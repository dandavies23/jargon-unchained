import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)



# Main dictionary routes
@app.route("/")
@app.route("/get_jargon")
def get_jargon():
    jargon = list(mongo.db.jargon.find().sort("_id", -1))
    return render_template("jargon.html", jargon=jargon)
# lists jargon newest first for relevancy and encourage contribution


# Homepage splash which introduces the Jargon Unchained concept
@app.route("/home")
def load_homepage():
    # will need to add shuffle logic here

    # jargon = mongo.db.jargon.aggregate([ { $sample: { "size": 1 } } ])
    return render_template("home.html")

# returns the list alphabetically
@app.route("/az_jargon")
def az_jargon():
    jargon = list(mongo.db.jargon.find().sort("jargon_name", 1))
    return render_template("jargon.html", jargon=jargon)


# returns the list reverse alpha
@app.route("/za_jargon")
def za_jargon():
    jargon = list(mongo.db.jargon.find().sort("jargon_name", 1))
    return render_template("jargon.html", jargon=jargon)


# returns the list in random order 
@app.route("/rand_jargon")
def rand_jargon():
    jargon = list(mongo.db.jargon.aggregate([{'$sample': {'size': 10 }}]))
    return render_template("jargon.html", jargon=jargon)

# returns the list by score
@app.route("/rank_jargon")
def rank_jargon():
    jargon = list(mongo.db.jargon.find())
    for i in range(len(jargon)):
        jargon[i]["love_percent"] = int(jargon[i]["love_percent"])
    jargon = sorted(jargon, key=lambda i: (i['love_percent']))
    return render_template("jargon.html", jargon=jargon)


# increments love percent by 1
@app.route("/like/<entry_id>")
def like(entry_id):
    entry = mongo.db.jargon.find_one({"_id": ObjectId(entry_id)})
    value = int(entry["love_percent"])
    value += 1
    value = str(value)
    mongo.db.jargon.update_one({"_id": ObjectId(entry_id)},
                               {"$set": {
                                   "love_percent": value
                               }})
    return redirect(url_for("get_jargon"))


# decrements love percent by 1
@app.route("/dislike/<entry_id>")
def dislike(entry_id):
    entry = mongo.db.jargon.find_one({"_id": ObjectId(entry_id)})
    value = int(entry["love_percent"])
    value -= 1
    value = str(value)
    mongo.db.jargon.update_one({"_id": ObjectId(entry_id)},
                               {"$set": {
                                   "love_percent": value
                               }})
    return redirect(url_for("get_jargon"))


# search based on query in MongoDB
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    jargon = list(mongo.db.jargon.find({"$text": {"$search": query}}))
    return render_template("jargon.html", jargon=jargon)


# Register wiring
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if real name already exists in db
        existing_realname = mongo.db.users.find_one(
            {"realname": request.form.get("realname").lower()})

        if existing_realname:
            flash("Real name already exists. Got any middle names?")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "realname": request.form.get("realname").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                # returns to login screen for now
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            # returns to login screen for now
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        jargon = mongo.db.jargon.find({"created_by": username})
        return render_template("profile.html",
            username=username, jargon=jargon)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_jargon", methods=["GET", "POST"])
def add_jargon():
    if request.method == "POST":
        jargon = {
            "jargon_name": request.form.get("jargon_name"),
            "definition": request.form.get("definition"),
            "usage": request.form.get("usage"),
            "category_name": request.form.get("category_name"),
            "editorialise": request.form.get("editorialise"),
            "created_by": session["user"],
            "love_percent": "55"
        }
        # add added default love percent score to entry
        mongo.db.jargon.insert_one(jargon)
        flash("Jargon added to dictionary")
        return redirect(url_for("get_jargon"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_jargon.html", categories=categories)


# edit jargon protocol
@app.route("/edit_jargon/<entry_id>", methods=["GET", "POST"])
def edit_jargon(entry_id):
    if request.method == "POST":
        submit = {
            "jargon_name": request.form.get("jargon_name"),
            "definition": request.form.get("definition"),
            "usage": request.form.get("usage"),
            "category_name": request.form.get("category_name"),
            "editorialise": request.form.get("editorialise"),
            "created_by": session["user"],
            "love_percent": request.form.get("love_percent")
        }
        # add rating to dictionary? or create as separate field?
        mongo.db.jargon.update({"_id": ObjectId(entry_id)}, submit)
        flash("Jargon updated")

    entry = mongo.db.jargon.find_one({"_id": ObjectId(entry_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_jargon.html", entry=entry, categories=categories)


# delete jargon
@app.route("/delete_jargon/<entry_id>")
def delete_jargon(entry_id):
    mongo.db.jargon.remove({"_id": ObjectId(entry_id)})
    flash("Jargon entry deleted")
    return redirect(url_for("get_jargon"))


# categories
@app.route("/get_categories")
def get_categories():
    # sort categories alphabetically and return as list
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New category added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category sucessfully updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category successfully deleted")
    return redirect(url_for("get_categories"))


@app.route("/load_databases/")
def load_databases():
    mongo.db.jargon.insert_many([
    {"jargon_name":"Impact, vb.",
        "definition":"To make an impact",
        "usage":"'How is this going to impact on the Q2 profit margin?'",
        "category_name":"Nouns as verbs",
        "editorialise":"‘Impact’ is just one example: this entry is a general comment on the appropriation of nouns as verbs. Seemingly going against one of the rules outlined earlier (simpler is better), seeing as ‘impact’ is more concise than ‘make an impact on’, this is actually more a textbook example of one of jargon’s most endemic problems. The first recorded usage of a noun as a verb could have been decades ago, but the business world’s gleeful adoption of the technique could be the most damaging thing that jargon has done to the English language.\r\n \r\nSo commonly used it’s basically normal English, the verb ‘to impact’ has made a big impact. Its influence on our language is widespread and myriad, and it helped open the floodgates for any noun to be turned into a verb. The mother tongue is poorer for it. \r\n\r\nWhether ‘impact’ itself will last is up for debate, but the general trend is here and will be all pervasive and all consuming within a number of years.","created_by":"lenguff","love_percent":"50"},
    {"jargon_name":"Cascade",
        "definition":"To disseminate information from the most important people to the least important people in a team, or more widely, a business.",
        "usage":"The minutes from the meeting were cascaded down through the organisation.",
        "category_name":"Nouns as verbs",
        "editorialise":"Since modern leadership in 21st century business is all about ‘facilitation’ and ‘employee empowerment’, rather than ‘command and control’-style upper-echelon bastardry, managers have been left lacking in ways to express their superiority over the common worker bee. Step forward the verb ‘to cascade'. \r\n‘Cascade’, as verb or noun, conjures up waterfalls, dreams that you want to go on forever. But mostly waterfalls. There’s an intrinsic artiness to the word that doesn’t work when talking about meeting minutes and the direction of flow of emails. But that didn’t deter some line manager into fantasy art who decided to needlessly complicate the process of sending emails to people. ‘Cascade’ doesn’t sound sexy; it manages to passive-aggressively state its faux-superiority over you, when the word ‘send’ would suffice. \r\nEmail will eventually die out as an antiquated communicating technology, but something will need to replace it, and there will always be meetings of managers that need to be minuted, summarised and that information then sent to people. The verb ‘to cascade’ is a relative newbie in the jargon game so it’s too early to tell how long it will last. (Not long, hopefully).","created_by":"dandavies23","love_percent":"23"},
    {"jargon_name":"Best practice",
        "definition":"The ‘best’ way to run your business. The ‘industry standard’, of whichever industry’s standards you are talking about.",
        "usage":"Blandco specialises in best practice solutions for the modern office environment",
        "category_name":"Overcomplicated",
        "editorialise":"There’s no simpler term for ‘best practice’ - but one isn’t needed. This makes the list as it’s a good example of a term that was invented to differentiate the service of a particular company from its competitors but has since been adopted by the whole industry and lost its original meaning. All law firms would claim their HR departments adhered to ‘best practice’, but who decides that? A company specialising in ‘best practice’ best practice, or best ‘best practice’ practice? And how would they come to that conclusion? The cycle goes on and on. The problem here is the idea of ‘best practice’ because not long ago, someone somewhere in the management chain decided that the average worker couldn’t be trusted to make a decision to the best of their abilities and needed some guidelines to tell them their right from wrong. \r\nEmployees learn, work and complete process-based tasks in different ways. Trying to make a diverse workforce behave in the same way is counter-productive at best. At worst it stifles creativity and invention, and demotivates to the point of apathy.","created_by":"admin","love_percent":"43"},
    {"jargon_name":"Best practice",
        "definition":"The ‘best’ way to run your business. The ‘industry standard’, of whichever industry’s standards you are talking about.",
        "usage":"Blandco specialises in best practice solutions for the modern office environment",
        "category_name":"Overcomplicated",
        "editorialise":"There’s no simpler term for ‘best practice’ - but one isn’t needed. This makes the list as it’s a good example of a term that was invented to differentiate the service of a particular company from its competitors but has since been adopted by the whole industry and lost its original meaning. All law firms would claim their HR departments adhered to ‘best practice’, but who decides that? A company specialising in ‘best practice’ best practice, or best ‘best practice’ practice? And how would they come to that conclusion? The cycle goes on and on. The problem here is the idea of ‘best practice’ because not long ago, someone somewhere in the management chain decided that the average worker couldn’t be trusted to make a decision to the best of their abilities and needed some guidelines to tell them their right from wrong. \r\nEmployees learn, work and complete process-based tasks in different ways. Trying to make a diverse workforce behave in the same way is counter-productive at best. At worst it stifles creativity and invention, and demotivates to the point of apathy.","created_by":"admin","love_percent":"43"},
    {"jargon_name":"Blue sky thinking",
        "definition":"Use your imagination",
        "usage":"We need to blue sky think this through",
        "category_name":"Overcomplicated","editorialise":"","created_by":"admin","love_percent":"31"},
    {"jargon_name":"Core competencies","definition":"The word ‘skills’ would probably do, when referring to an individual’s abilities",
        "usage":"Blandco’s core competencies are people management, stream- lined processes and maximising revenue",
        "category_name":"Overcomplicated",
        "editorialise":"It was used as far back as the 80s, but ‘core competencies’ came to the fore in the 2000s. Does this reflect that the average workforce is getting cleverer? I’d say perhaps the opposite. The need to measure everything often masks a fundamental deficiency. \r\nThe addition of the word ‘core’ actually undermines the meaning of the word ‘competency’. It implies that some people have things they know a bit about but aren’t very good at, which is the case for most people, but you wouldn’t refer to them as regular competencies would you? The existence of the phrase ‘core competencies’ is symptomatic of the modern need to compartmentalise our existence. ‘Skills’ works better. It encompasses everything you can do, understanding that some might be more developed than others. How long before another word is added? Inner core competencies? Singular core competencies? Key core competencies? \r\nThis one is most likely here for the long haul. ‘Core competency’ will continue to blight employee CVs and the ‘about’ tab of company websites for a long time yet. As a rule of thumb, the longer a jargon term has been around, the harder it is to shake off, as it disappears into the English language.\r\n","created_by":"lenguff","love_percent":"32"},
    {"jargon_name":"Cover off",
        "definition":"To cover",
        "usage":"Now that’s been covered off, let’s move on to discuss your appraisal",
        "category_name":"Overcomplicated",
        "editorialise":"The word ‘off’ is unnecessary. What is being covered isn’t any more covered because its been ‘covered off’, and if whoever invented this neologism to make him/herself sound insightful thinks it is, they are confusing the verb ‘to cover’ with the verb ‘to complete’. It’s as if saying something is covered is not quite final enough. It’s covered, but is it really covered? Can it be covered more? To argue its case, you might say that to ‘cover’ something in the present tense would be to discuss something, a meeting for example, so after something was discussed it would be covered off, but it would be overly generous to allow the jargonista that kind of leeway. As businesses move to an ever more task-based, stats-based, ‘data’- based work environment, its clear that ‘cover off’ is not going away. Perhaps you could ask the next person at your work who uses it to explain the essential differences between something being covered and covered off? That would be a funny, if awkward, conversation. ","created_by":"lenguff","love_percent":"80"},
    {"jargon_name":"Ducks in a row","definition":"To be organised","usage":"You need to make sure you have all your ducks in a row before the audit next week","category_name":"Plain nonsense","editorialise":"It’s been around a while but oddly its adoption isn’t as widespread as, say, ‘blue sky thinking’. \r\nIt’s an inaccurate metaphor. Saying ‘to be organised’ is clearer and more concise, so is the preferable option to this nonsense. No-one associates ducks with business, and although that isn’t how metaphors work, the ducks analogy falls down mainly for this reason: telling someone to ‘get their ducks in a row’ is saying ‘you need to forcibly organise yourself’, whereas the natural phenomenon it is comparing itself to is instinctive and genetic. Unless you are predicting some kind of cosmic alignment that makes spreadsheets fill themselves and signs invoices automatically, then what we are looking at here is a visual metaphor that doesn’t stand up to basic scrutiny. \r\nLuckily this one doesn’t seem that popular, despite its having been around for a while. This is most likely because the majority of Standard English-speaking people realise that it sounds ridiculous, even if they implicitly understand the vague comparison (because they can visualise what some identical objects in a row look like and work backwards to understand what the jargon means).","created_by":"lenguff","love_percent":"56"},
    {"jargon_name":"Face time","definition":"To talk to each other face to face","usage":"We need to book some face time in to tie up the Mexico deal","category_name":"Overcomplicated","editorialise":"Around since the 80s, this probably gained widespread popularity after the explosion of social networks. \r\nSince when did the original - and best - way of communicating need to be repackaged for a new generation? I’m a staunch advocate of social networks and have been for many years, and I never have, and never will, use the expression ‘face time’. Talking to each other is simple, so let's keep talking about talking to each other simple too \r\nThe term has been co-opted by Apple, so it looks as if it’s here for good. If Apple starts to decline then maybe its associated trademarks may do too, of which FaceTime (note the caps) is one. As travel gets more expensive and remote working becomes more popular (we’ll ignore Yahoo CEO Marissa Meyer’s recent-ish outburst), meeting up in person will be at a premium. All hail king FaceTime. We bow at your needless feet. ","created_by":"lenguff","love_percent":"21"},
    {"jargon_name":"Going forward","definition":" In future","usage":"We need to rethink our media partners strategy going forward, particularly beyond 2025","category_name":"Plain nonsense","editorialise":"Of the whole list, this is one of the most-used, and most popular to the point where it has been almost subsumed into normal English. Popular since the 70s, ‘going forward’ scores low in the offensive stakes, but this is most likely because we are now blind (deaf?) to its absurdity. \r\nWhile ‘going forward’ supposedly means the same as ‘in future’, it implies a sense of progress that ‘in future’ doesn’t. The use of the word ‘forward’ conjures up feelings of progress and extreme productivity, a sense of control over one’s professional destiny, whereas ‘in future’ is nakedly fatalistic, implying powerlessness at the hands of time. As we all know, ‘going forward’ really means ‘let’s address these issues in some more meetings in a few months, but let’s sound like we have some radical forward-thinking ideas we can do something with right now.’ \r\nTo put their destiny back in their own hands, workers could start staying ‘in the future’, as if blessed with the power of prescience and divination. That might not endear you too much to your co-workers. No-one likes a clever-clogs.","created_by":"lenguff","love_percent":"25"},
    {"jargon_name":"Granular","definition":"Detailed","usage":"Let’s look at the data at a more granular level","category_name":"Overcomplicated","editorialise":"We’re all busy people these day. We don’t have a lot of time to spend in each meeting. We only want to know the basics of each project; the ‘top-line numbers’, the ‘high-level’ stuff. If we need a better picture of something it had better sound pretty special. Step forward, ‘granular’. Perhaps because, more than ever, time and resource constraints (do more with less blah blah blah) mean that we rarely get to the level of detail that was previously the norm. \r\nNo-one likes all those details, but if it’s granular? That sounds exciting! To look at something at a granular level, you often need to ‘drill down’ into the data. Find me a geologist who uses a drill to find granules and I’ll show you someone who bought their degree from realdegreez.com. It’s not uncommon for business jargon to mix its metaphors, I’d venture that it’s commonplace in fact, and this is one of the best. Essentially, it’s wrong because it’s committed the most insidious crime in all of business jargon. Inventing new contexts to overcome the stigma of words that are now ‘tainted’ with bad business juju - or maybe just reality. So, problems become ‘issues’, and even 'opportunities'. ","created_by":"lenguff","love_percent":"43"},
    {"jargon_name":"Interrogate the data","definition":"Look at the data in detail","usage":"We need to really interrogate the data to understand our audience","category_name":"Overcomplicated","editorialise":"As ‘big data’ and data journalism have come to the fore in recent times, so has the jargonista’s pastime of ‘interrogating’ the data. Maybe old school journalists have decided to apply interviewing, one of their previous core competencies, to this new strain of journalism. Maybe if the data doesn’t yield the information required then the next step is ‘waterboarding the data’ or putting the data in stress positions. \r\nFirst, using the verb ‘to interrogate’ is way too aggressive a way to put it. Second, interrogation is usually part of a dialogue. The data, whatever it (or they) maybe isn’t going to respond, it’s just going to sit there, being data. A load of unresponsive zeroes and ones. It’s another common trope of business jargon. Take an idea, a method, an existing process, and misguidedly try to go one better, to make it look like you’re working harder or bringing something new to the table. \r\nIt’s a term that’s in its infancy. Who knows if it’ll make an impact. ‘Big data’ is certainly an idea that looks settled in even if the ‘big’ part lacks definition. And data needs to be looked at and queried. Maybe shouted at occasionally with an angle-poise lamp shone in its face.","created_by":"lenguff","love_percent":"10"},
    {"jargon_name":"Leverage","definition":"To make use of in a situation","usage":"We should leverage our assets to provide the best ROI for the business","category_name":"Overcomplicated","editorialise":"It should be acknowledged that the verb ‘to leverage’ has a meaningful use in certain financial situations. Leveraged dealing is ‘the acquisition of another company using a significant amount of borrowed money (bonds or loans) to meet the cost of acquisition’, however that doesn’t mean that its use in the financial sector is always in an appropriate context and is never jargon. More that, like a lot of the jargon, the word has been taken out of context and applied to similar scenarios where no actual leveraging is being done. \r\nIt’s replacing the word ‘use’ with something more complicated, that doesn’t have quite the same meaning. Whenever the word ‘leverage’ is used, it assumes you have the upper hand in the transaction. Its use makes you lie to yourself that you do. It again makes you appear to be doing work that you’re not actually doing, talking from a position that you don’t actually hold. \r\nThis is embedded like a tick under the skin of plain English, but it’s never coming out. Leverage is the deal breaker, the corporate icing on the business cake. The Babel Fish that lets your clients know you talk the right language - even if you don’t understand basic grammar and spelling.","created_by":"lenguff","love_percent":"58"},
    {"jargon_name":"Monetise","definition":"Make money from","usage":"To maximise revenue we have to monetise our peripheral customer base","category_name":"-ise","editorialise":"This is a specific example of the general malaise afflicting the jargon world, as mentioned before, and that’s turning nouns into verbs, at whatever cost. And if it doesn’t sound quite right, even to the oblivious ears of the jargonista, stick an ‘-ise’ on the end and you’re golden. But, as with the word ‘money’, the end product isn’t ‘moneyise’ but ‘monetise’, indicating that some of the implicit rules of our idiosyncratic language are not lost even on the most confused exponents of the mother tongue. ‘Monetise’ is included because it’s the perfect example of the unnecessary need to create verbs out of everything at any cost. It’s included because it’s the perfect example of the avarice that underlies the motives of the true die-hard adherents of business jargon. It’s included because monetise is not a verb \r\nThe perceived fluctuation of income and profit means that every- thing is there to be made money out of. Your local church probably has a high st coffee chain, scoping the place out already. ","created_by":"dandavies23","love_percent":"76"},
    {"jargon_name":"On the same page","definition":"To understand each other","usage":"I just wanted to catch up before the quarterly meeting to check we’re on the same page","category_name":"Tortured metaphors","editorialise":"This feels like one of the less offensive phrases in the world of business jargon, and that’s primarily because it’s been here for a while. It could have a more sinister history than you think though. Either: it’s a mild, explanatory, one might say almost appropriate metaphor for understanding each other. After all, you regularly flick through pages of notes during meetings don’t you? Or: it’s a watered down version of ‘singing from the same hymn sheet’ - one of the most ridiculous metaphors in the world of business jargon, and one of the original reasons the world was alerted to the very existence of this crooked version of our language. \r\nIf you have to confirm with a colleague that ‘you’re on the same page’, the chances are you’re not. But you couldn’t say ‘just making sure we understand each other’, could you? That would be confrontational. And there we are again. Avoiding issues with complex language. Classic jargon. If it was originally a watered-down, less obnoxious way of asking everyone if they’re ‘singing from the same hymn sheet’, then it’s first for the chop. Don’t confuse the minutiae of a business meeting with making music. Ever. ","created_by":"admin","love_percent":"55"},
    {"jargon_name":"Solution","category_name":"Plain nonsense","created_by":"lenguff","definition":"An object. A product. A service. Almost anything in the jargon world","editorialise":"We all want solutions to our problems don’t we? Not just in the world of business, but in life. Life is a neverending journey of obstacles, disappointments and challenges, and if all these problems could be solved, then...wow. \nNot everything can be a solution [16]. Some things described as ‘solutions’ are just helpful. Others aren’t even that. It’s a business’s job (maybe even its raison d’etre) to understand its customers. This is why so much money is spent on market research. ‘Customer insight’ and other similar studies. But in most cases, it’ll be the customer who determines whether a particular product is ‘the solution’ after they’ve used it, not the business deciding its newest product is ‘the solution’ before it even has customers to use it. \nThe converse to this is equally annoying. There are many products/methods/’things’ called solutions that are perfectly good, but there was never a problem in the first place. No impasse to get through, no river to cross. Just a few different ways of doing business or living life. But the bedrock of consumerism is fear. The way you do things now is no good. This is why it’s a problem. Here is a solution. And so on. \nNow that the word solution has been devalued into meaninglessness - Journalist Tim Phillips brilliantly calls it ‘semantic inflation’ - we have the ‘turnkey’ variant. An actual solution, rather than a pretend ‘solution’. Confused? Welcome to Jargonsville, population indeterminate. \nThere is no solution to the word solution. From drainage to haulage to office supplies to cake decorations, solutions are everywhere. ","love_percent":"35","usage":"Blandco offers a wide range of solutions to your business needs"},
    {"jargon_name":"Strategic alliance","definition":"A partnership","usage":"Blandco are delighted to have formed a new strategic alliance with Panmedia as media partners for ","category_name":"Overcomplicated","editorialise":"‘Strategic’ is THE go-to prefix to make it sound like you’re getting stuff done. \r\nLots of aspects of business life are inherently strategic. If they weren’t they would be disorganised. So, ‘strategic’ has less and less meaning and there increasingly is almost no context in which it adds any use to any sentence. That is an essential quality to deciding whether something is jargon. However, one meaning you can infer from the use of the word ‘strategic’ is when used with the word ‘partner’, which actually makes the pairing vaguer, in that you know a strategic partnership will be one that isn’t judged on short term results, so possibly never accountable ‘going forward’.\r\n‘Strategic’ is a key player in any internal meeting. It makes it sound like you’re doing stuff when you aren’t; this one will become more and more popular until everything is strategic and then the concept will have to reinvent itself again. Perhaps with the addition of a ‘key’ or a ‘core’ on the front. ","created_by":"dandavies23","love_percent":"55"},
    {"jargon_name":"Think outside the box","definition":"To think differently","usage":"Try and think outside the box on this project","category_name":"Plain nonsense","editorialise":"Everyone has heard this one before, and it continues to blight meetings of every size and subject globally. \r\n‘Think outside the box’ is a tacit admission that no-one in your average business has any good ideas. What is the box? How big is it? Is it a two-dimensional box such as you might find on a football pitch, or a three-dimensional box that you might use in a house move? Either way your normal ideas are inside it and they are no good. It’s a concept that is entirely subjective and means something different to everyone, therefore is rendered useless when applied to a group setting. What Jargonistas are really saying is ‘can you come up with an idea that doesn’t involve Microsoft PowerPoint.’ \r\nAlmost outmoded and replaced by the more multipurpose adjective ‘smart’, ‘thinking outside the box’ is one of the old men of business jargon, alongside ‘blue sky thinking’ and ‘going forward’. As long as there are thought showers, people will be asked to think outside the box. But no-one wants to get wet do they? ","created_by":"admin","love_percent":"6"}
    ])
    # mongo.db.jargon.insert_many([
      #   {"jargon_name": "Test", "definition": "This is a test",
        #  "usage": "Test right here",
        #  "category_name": "Nouns as verbs",
        #  "created_by": "lenguff", "love_percent": "50"},
       #  {"jargon_name": "Another test", "definition": "Test again",
        #  "usage": "How would you?",
       #   "category_name": "Nouns as verbs", "editorialise": "",
       #   "created_by": "dandavies23", "love_percent": "23"},
    # ])
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
