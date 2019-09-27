from class_artist import Artist
from class_artwork import Artwork
from test_data import *
from peewee import *

# Assign database
db = SqliteDatabase('artstore_db.sqlite')

def create_data_base():
    # Create the database connection to a db file
    db.connect()
    tables = db.get_tables()
    # If there are no tables in the db then add this base data
    if len(tables) == 0:
        db.create_tables([Artist])
        db.create_tables([Artwork])
        add_test_data()
    db.close()

def add_new_artist_to_db(name, email):
    db.connect()
    # Add the new artist to the db
    new_artist = Artist.Artist(name=name, email=email)
    new_artist.save()
    db.close()


def search_db_for_artwork_by_artist(name):
    db.connect()
    # Locate all artwork with the corresponding name
    artwork_list = Artwork.select().where(Artwork.Artwork.artist == name)
    # Display all artwork 
    db.close()
    return artwork_list