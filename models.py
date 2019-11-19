import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String(120))
    state = Column(String(120))
    address = Column(String(120))
    phone = Column(String(120))
    image_link = Column(String(500))
    facebook_link = Column(String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String(120))
    state = Column(String(120))
    phone = Column(String(120))
    genres = Column(String(120))
    image_link = Column(String(500))
    facebook_link = Column(String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


class Show(db.Model):
    __tablename__ = 'Show'

    id = Column(Integer, primary_key=True)
    venue_id = Column(Integer)
    venue_name = Column(String(120))
    artist_name = Column(String(120))
    artist_image_link = Column(String(120))
    start_time = Column(String(120))
