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

# Homepage splash which introduces the Jargon Unchained concept
@app.route("/")
@app.route("/home")
def load_homepage():
    jargon = mongo.db.jargon.aggregate([{'$sample': {'size': 1 }}])
    return render_template("home.html", jargon=jargon)

@app.route("/about")
def load_about():
    return render_template("about.html")


# Main dictionary routes
@app.route("/get_jargon")
def get_jargon():
    jargon = list(mongo.db.jargon.find().sort("_id", -1))
    return render_template("jargon.html", jargon=jargon)
# lists jargon newest first for relevancy and encourage contribution


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
    mongo.db.jargon.delete_one({"_id": ObjectId(entry_id)})
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
    # mongo.db.jargon.insert_many([
      #  use importdb.py as a fixture ])
    return redirect(url_for("load_homepage"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
