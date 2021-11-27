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
        flash("You're locked and loaded!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back {}".format(request.form.get("username")))
            else:
                #invalid password
                flash("Wrong handle and/or password")
                return redirect(url_for("login")) # returns to login screen for now

        else:
            # username doeesn't exist
            flash("Wrong handle and/or password")
            return redirect(url_for("login")) # returns to login screen for now
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
