"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class User(db.Model):
    """User of Shoe Spotting website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id,
                                               self.email)


class Post(db.Model):
    """Posts of a shoe by a user."""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    img_url = db.Column(db.String(100), nullable=True)
    added_at = db.Column(db.DateTime)
    title = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    text = db.Column(db.String(200))

    #Define relationship with User table 
    user = db.relationship("User", backref='posts')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Post post_id=%s img_url=%s added_at=%s title=%s user_id=%s text=%s>" % (self.post_id, self.title, self.user_id,
                                                 self.img_url, self.added_at, self.text)


class Comment(db.Model):
    """Comment of a post by a user."""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)
    user_id = db.Column(db.Integer,
                         db.ForeignKey('users.user_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    text = db.Column(db.String(200))
    added_at = db.Column(db.DateTime)

    #Define a relationship to Users
    user = db.relationship("User", backref='comments')

    #Define a relationship to Posts

    post = db.relationship("Post", backref='comments')

    
    def __repr__(self):
        """Provide helpful representation when printed."""

        s = "<Comment comment_id=%s user_id=%s post_id=%s text=%s added_at=%s>"
        return s % (self.comment_id, self.user_id, self.post_id,
                    self.text, self.added_at)


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///shoespotting'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
