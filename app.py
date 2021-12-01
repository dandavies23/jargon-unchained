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


@app.route("/")
@app.route("/get_jargon")
def get_jargon():
    jargon = list(mongo.db.jargon.find())
    return render_template("jargon.html", jargon=jargon)


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
                return redirect(url_for("login")) # returns to login screen for now

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login")) # returns to login screen for now

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)   
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
            "created_by": session["user"]
        }
        # add rating to dictionary? or create as separate field?
        mongo.db.jargon.insert_one(jargon)
        flash("Jargon added to dictionary")
        return redirect(url_for("get_jargon"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_jargon.html", categories=categories)


@app.route("/edit_jargon/<entry_id>", methods=["GET", "POST"])
def edit_jargon(entry_id):
    if request.method == "POST":
        submit = {
            "jargon_name": request.form.get("jargon_name"),
            "definition": request.form.get("definition"),
            "usage": request.form.get("usage"),
            "category_name": request.form.get("category_name"),
            "editorialise": request.form.get("editorialise"),
            "created_by": session["user"]
        }
        # add rating to dictionary? or create as separate field?
        mongo.db.jargon.update({"_id": ObjectId(entry_id)}, submit)
        flash("Jargon updated")
    
    entry = mongo.db.jargon.find_one({"_id": ObjectId(entry_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_jargon.html", entry=entry, categories=categories)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)