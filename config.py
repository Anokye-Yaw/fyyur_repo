import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database



# TODO IMPLEMENT DATABASE URL
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:test1@localhost:5432/fyyurdb'

class DatabaseURI:
    # Just change the names of your database and credentials and all to connect to your local system
    DATABASE_NAME = "fyyurdb"
    username = 'postgres'
    password = 'test1'
    url = 'localhost:5432'

    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        username, password, url, DATABASE_NAME)