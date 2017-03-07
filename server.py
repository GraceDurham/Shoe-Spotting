"""Shoe Ratings."""

from jinja2 import StrictUndefined
import sqlalchemy

from flask import Flask, render_template, request, flash, redirect, jsonify, session, url_for
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Post, Comment

from datetime import datetime
from flask import jsonify


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Welcome page"""
    return render_template("welcome.html")



@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""
    print "hello"
    # Get form variables
    first_name = request.form["first name"]
    last_name = request.form["last name"]
    email = request.form["email"]
    password = request.form["password"]
    
    new_user = User(email=email, password=password, first_name=first_name, last_name=last_name)

    db.session.add(new_user)
    db.session.commit()

    flash("Yay! User %s %s added." % (first_name, last_name))
    return redirect ("/")


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

    if not user:
        flash("No such user please register first")
        return redirect("/register")

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
    return render_template("profile.html", posts=posts)


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

    posts = Post.query.filter_by(user_id=session["user_id"]).all()

    return render_template("profile.html", posts=posts)


@app.route('/add-post', methods=['GET'])
def pop_add_post():
    """ Displays the form"""

    return render_template("add_post.html")


@app.route('/add-post', methods=['POST'])
def add_post():
    """add post to the database and return feed"""

    img_url = request.form["img_url"]
    title = request.form["title"]
    website_url = request.form["website_url"]
    text = request.form["text"]

    added_at = datetime.now()

    user_id = session["user_id"]
    
    new_post = Post(img_url=img_url, title=title, website_url=website_url, text=text, user_id=user_id, added_at=added_at)

    db.session.add(new_post)
    db.session.commit()


    return redirect("/profile")


@app.route('/add-comment', methods=['POST'])
def add_comment():
    """ add comment to the database"""


    comment = request.form.get("comment")
    post_id = request.form.get("post_id")

    added_at = datetime.now()

    user_id = session["user_id"]


    new_comment = Comment(user_id=user_id, post_id=post_id, comment=comment, added_at=added_at)


    db.session.add(new_comment)
    db.session.commit()
    formatted_added_at = added_at.strftime("%b %d, %Y")
    
    return jsonify({"comment": comment, "added_at": formatted_added_at, "first_name": new_comment.user.first_name, "last_name": new_comment.user.last_name})


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    post = Post.query.get(post_id)

    return render_template("post.html", post=post)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
