from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from flask_migrate import Migrate
from flask import Flask
from flask_moment import Moment
#import dateutil.parser



# TODO: connect to a local postgresql database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test1@localhost:5432/fyyurdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship("Show", backref="Venue", lazy=False)
    


    def __repr__(self):
        return f"<Venue id={self.id} name={self.name} city={self.city} state={self.city}> \n"

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
#db.create_all()

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
   
    shows = db.relationship("Show", backref="Artist", lazy=False, cascade="all, delete-orphan")
    

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
   __tablename__ = "Show"
   
   id = db.Column(db.Integer, primary_key=True, unique=True)
   artist_id = db.Column(db.Integer, db.ForeignKey("Artist.id"), nullable=False)
   venue_id = db.Column(db.Integer, db.ForeignKey("Venue.id"), nullable=False)
   start_time = db.Column(db.DateTime, nullable=False)
   artist = db.relationship('Artist', backref='Show', lazy=True)
   venue = db.relationship('Venue', backref='Show', lazy=True)

   #def __repr__(self):
      #return f"<Show id={self.id} artist_id={self.artist_id} venue_id={self.venue_id} start_time={self.start_time}"
