"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func

from model import User, connect_to_db, db
from server import app


def load_users():
    """Load users from u.user into database."""

    grace = User.query.filter_by(email="gracelee.durham@gmail.com").first()

    if(grace == None):
        grace = User(email="gracelee.durham@gmail.com", password="password")
        db.session.add(grace)
        db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
  
