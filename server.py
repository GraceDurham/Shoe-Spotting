"""Shoe Ratings."""

from jinja2 import StrictUndefined
import sqlalchemy

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Post, Comment

from datetime import datetime


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Welcome page"""
    return render_template("Welcome.html")


# @app.route('/register', methods=['GET'])
# def register_form():
#     """Show form for user signup."""

#     return render_template("register_form.html")


# @app.route('/register', methods=['POST'])
# def register_process():
#     """Process registration."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]
#     age = int(request.form["age"])
#     zipcode = request.form["zipcode"]

#     new_user = User(email=email, password=password, age=age, zipcode=zipcode)

#     db.session.add(new_user)
#     db.session.commit()

#     flash("User %s added." % email)
#     return redirect("/")


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()
    print user.user_id

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    posts = Post.query.filter_by(user_id = user.user_id).all()
    # print posts[0].img_url

    # query all the posts where user id = user id logged in 
    #get lists of different post ojects 
    # format it in the profile html with for loop jinja 
    # pass variable to render template so it is available in jijna

    flash("Logged in")
    return render_template("Profile.html", posts=posts)


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")

@app.route('/feed')
def feed():
    """Gets posts for all the posts"""
    posts = Post.query.all()

    return render_template("shoefeed.html", posts=posts)


@app.route('/profile')
def profile():
    """ User logs in and takes user to profile page"""

    posts = Post.query.filter_by(user_id = session["user_id"]).all()

    return render_template("Profile.html", posts=posts)


@app.route('/add-post', methods=['GET'])
def pop_add_post():
    """ Displays the form"""



    return render_template("add_post.html")

@app.route('/add-post', methods=['POST'])
def add_post():
    """add post to the database and return feed"""

    print request.form

    img_url = request.form["img_url"]
    title = request.form["title"]
    text = request.form["text"]

    added_at = datetime.now()

    user_id = session["user_id"]
    
    new_post = Post(img_url=img_url, title=title, text=text, user_id=user_id, added_at=added_at)

    db.session.add(new_post)
    db.session.commit()


    return redirect("/profile")

@app.route('/add_comment')
def pop_add_comment():
    """ Allows users to add comments when click on add-comment button on feed"""

    pass

    return render_template("add_comment.html")


@app.route('/add_comment', methods=['Post'])
def add_comment():
    """ add comment to the database"""

    pass

    return rendertemplate("shoefeed.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
