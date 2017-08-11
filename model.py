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
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s first_name=%s last_name=%s email=%s>" % (self.user_id,
                                    self.first_name, self.last_name, self.email)


class Post(db.Model):
    """Posts of a shoe by a user."""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    website_url = db.Column(db.String(800), nullable=True)
    img_url = db.Column(db.String(800), nullable=True)
    added_at = db.Column(db.DateTime)
    title = db.Column(db.String(800))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    text = db.Column(db.String(800))

    #Define relationship with User table 
    user = db.relationship("User", backref='posts')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Post post_id=%s website_url=%s img_url=%s added_at=%s title=%s user_id=%s text=%s>" % (self.post_id, self.website_url, self.title, self.user_id,
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
    comment = db.Column(db.String(1000))
    added_at = db.Column(db.DateTime)

    #Define a relationship to Users
    user = db.relationship("User", backref='comments')

    #Define a relationship to Posts

    post = db.relationship("Post", backref='comments')

    
    def __repr__(self):
        """Provide helpful representation when printed."""

        s = "<Comment comment_id=%s user_id=%s post_id=%s comment=%s added_at=%s>"
        return s % (self.comment_id, self.user_id, self.post_id,
                    self.comment, self.added_at)

    def example_data():
        """Create some sample data."""

        img_url = "https://www.hautelookcdn.com/resizer/434x650/products/JS2005/large/6156640.jpg"
    
        added_at = datetime.now()
        title = "Online Nordstrom Rack"
        text = "Jessica Simpson Madison ballet flats only $29.99 usually $69.99"
        user = User.query.filter_by(email="gracelee.durham@gmail.com").one()
        user_id = user.user_id

        post1 = Post(img_url=img_url, added_at=added_at, title=title, text=text, user_id=user_id)

        db.session.add(post1)
        db.session.commit()


#####################################################################
# Helper functions

def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///shoespotting'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
