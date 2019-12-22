from sqlalchemy import Column, String, Integer, Boolean, ARRAY, DateTime, create_engine, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    genres = db.Column(ARRAY(String()), nullable=False)
    address = db.Column(String(120), nullable=False)
    city = db.Column(String(120), nullable=False)
    state = db.Column(String(120), nullable=False)
    phone = db.Column(String(120), nullable=False)
    website = db.Column(String(120))
    facebook_link = db.Column(String())
    seeking_talent = db.Column(Boolean, default=False)
    seeking_description = db.Column(String())
    image_link = db.Column(String(500), nullable=False)

    def __repr__(self):
        return f'<Venue {self.name, self.address, self.genres, self.shows}>'


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    genres = db.Column(ARRAY(String()), nullable=False)
    city = db.Column(String(120), nullable=False)
    state = db.Column(String(120), nullable=False)
    phone = db.Column(String(120), nullable=False)
    website = db.Column(String(120))
    facebook_link = db.Column(String())
    seeking_venue = db.Column(Boolean, default=False)
    seeking_description = db.Column(String())
    image_link = db.Column(String(500), nullable=False)

    def __repr__(self):
        return f'<Artist {self.id, self.name, self.genres, self.shows}>'


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(Integer, primary_key=True)
    venue_id = db.Column(Integer, ForeignKey(
        'Venue.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    artist_id = db.Column(Integer, ForeignKey(
        'Artist.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    start_time = db.Column(DateTime, nullable=False, default=datetime.utcnow())

    venue = db.relationship('Venue', backref=db.backref('shows', lazy=True))
    artist = db.relationship('Artist', backref=db.backref('shows', lazy=True))

    def __repr__(self):
        return f'<Show {self.id, self.start_time, self.artist}>'


# Seed data
artist1 = {
    "id": 4,
    "name": "Guns N Petals",
    "genres": ["Rock n Roll"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "326-123-5000",
    "website": "https://www.gunsnpetalsband.com",
    "facebook_link": "https://www.facebook.com/GunsNPetals",
    "seeking_venue": True,
    "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
    "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
}
artist2 = {
    "id": 5,
    "name": "Matt Quevedo",
    "genres": ["Jazz"],
    "city": "New York",
    "state": "NY",
    "phone": "300-400-5000",
    "facebook_link": "https://www.facebook.com/mattquevedo923251523",
    "website": None,
    "seeking_venue": False,
    "seeking_description": None,
    "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"
}
artist3 = {
    "id": 6,
    "name": "The Wild Sax Band",
    "genres": ["Jazz", "Classical"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "432-325-5432",
    "facebook_link": "https://www.facebook.com/mattquevedo923251523",
    "website": None,
    "seeking_venue": False,
    "seeking_description": None,
    "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"
}


venue1 = {
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
}
venue2 = {
    "id": 2,
    "name": "The Dueling Pianos Bar",
    "genres": ["Classical", "R&B", "Hip-Hop"],
    "address": "335 Delancey Street",
    "city": "New York",
    "state": "NY",
    "phone": "914-003-1132",
    "website": "https://www.theduelingpianos.com",
    "facebook_link": "https://www.facebook.com/theduelingpianos",
    "seeking_talent": False,
    "seeking_description": None,
    "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
}
venue3 = {
    "id": 3,
    "name": "Park Square Live Music & Coffee",
    "genres":  ["Rock n Roll", "Jazz", "Classical", "Folk"],
    "address": "34 Whiskey Moore Ave",
    "city": "San Francisco",
    "state": "CA",
    "phone": "415-000-1234",
    "website": "https://www.parksquarelivemusicandcoffee.com",
    "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
    "seeking_talent": False,
    "seeking_description": None,
    "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
}


show1 = {
    "id": 1,
    "venue_id": 1,
    "artist_id": 4,
    "start_time": "2019-05-21T21:30:00.000Z"
}

show2 = {
    "id": 2,
    "venue_id": 3,
    "artist_id": 5,
    "start_time": "2019-06-15T23:00:00.000Z"
}

show3 = {
    "id": 3,
    "venue_id": 3,
    "artist_id": 6,
    "start_time": "2035-04-01T20:00:00.000Z"
}

show4 = {
    "id": 4,
    "venue_id": 3,
    "artist_id": 6,
    "start_time": "2035-04-08T20:00:00.000Z"
}

show5 = {
    "id": 5,
    "venue_id": 3,
    "artist_id": 6,
    "start_time": "2035-04-15T20:00:00.000Z"
}
