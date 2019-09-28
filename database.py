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
    new_artist = Artist(name=name, email=email)
    new_artist.save()
    db.close()
    return new_artist


def search_db_for_artwork_by_artist(name):
    db.connect()
    # Locate all artwork with the corresponding name
    artwork_list = Artwork.select().where(Artwork.artist == name)
    # Display all artwork 
    db.close()
    return artwork_list


def search_db_for_available_artwork_by_artist(name):
    db.connect()
    # Locate all artwork with the corresponding name that is available
    artwork_list = Artwork.select().where(Artwork.artist == name, Artwork.available == True)
    # Display all available artwork 
    db.close()
    return artwork_list


def add_new_artwork_to_db(name, name_of_artwork, price, available):
    db.connect()  
    new_artwork = Artwork(artist=name, name_of_artwork=name_of_artwork, price=price, available=available)
    new_artwork.save()
    db.close()
    return new_artwork


def delete_artwork_in_db(name_of_artwork):
    db.connect()
    delete = Artwork.delete().where(Artwork.name_of_artwork == name_of_artwork).execute()
    db.close()
    return delete


def db_change_artwork_availability(name_of_artwork, availability):
    db.connect()
    updated_artwork = Artwork.update(available=availability).where(Artwork.name_of_artwork == name_of_artwork).execute()
    db.close()
    return updated_artwork