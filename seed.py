"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func

from model import User, Post, Comment, connect_to_db, db
from server import app
import time
from datetime import datetime


def load_users():
    """Load users into database."""


    grace = User(email="gracelee.durham@gmail.com", password="password")
    db.session.add(grace)
    db.session.commit()

## commenting out load posts because users are going to be inputting this info via Flask
def load_posts():
    """Load posts into database."""
    #deletes duplicates from the Post database when seed.py is ran

    img_url = "http://a3.zassets.com/images/z/3/9/0/2/7/5/3902757-p-MULTIVIEW.jpg"
    
    added_at = datetime.now()
    title = "test post 1"
    text = "Great shoes at Macy's"
    user = User.query.filter_by(email="gracelee.durham@gmail.com").one()
    user_id = user.user_id

    post1 = Post(img_url=img_url, added_at=added_at, title=title, text=text, user_id=user_id)

    db.session.add(post1)
    db.session.commit()

    img_url = "http://scene7.targetimg1.com/is/image/Target/14354227?wid=360&hei=360&qlt=80&fmt=pjpeg"

    added_at = datetime.now()
    title = "test post 2"
    text = "Great shoes at Nordstrom"
    user = User.query.filter_by(email="gracelee.durham@gmail.com").one()
    user_id = user.user_id

    post2 = Post(img_url=img_url, added_at=added_at, title=title, text=text, user_id=user_id)

    db.session.add(post2)
    db.session.commit()


    img_url = "https://s-media-cache-ak0.pinimg.com/originals/e7/fd/65/e7fd6591a37ebd61ac6e19d454df8d45.jpg"
    added_at = datetime.now()
    title = "test post 3"
    text = "Great shoes at Target"
    user = User.query.filter_by(email="gracelee.durham@gmail.com").one()
    user_id = user.user_id

    post3 = Post(img_url=img_url, added_at=added_at, title=title, text=text, user_id=user_id)

    db.session.add(post3)
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    grace = User.query.filter_by(email="gracelee.durham@gmail.com").first()
    
    #If grace is not there then we know we need to seed the database
    if(grace == None):
        load_users()
        load_posts()
  
