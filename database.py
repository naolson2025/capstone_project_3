from class_artist import Artist
from class_artwork import Artwork
from test_data import *
from peewee import SqliteDatabase

class Database():

    def __init__(self, db):
        self.db = db
        self.create_data_base()


    def create_data_base(self):
        database = SqliteDatabase(self.db)
        # Create the database connection to a db file
        database.connect()
        tables = database.get_tables()
        # If there are no tables in the db then add this base data
        if len(tables) == 0:
            database.create_tables([Artist, Artwork])
            #add_test_data()
        database.close()


    def add_new_artist_to_db(self, name, email):
        database = SqliteDatabase(self.db)
        database.connect()
        # Add the new artist to the db
        new_artist = Artist(name=name, email=email)
        new_artist.save()
        database.close()
        return new_artist


    def db_search_for_artist(self, name):
        database = SqliteDatabase(self.db)
        database.connect()
        artist = Artist.select().where(Artist.name == name)
        database.close()
        return artist


    def search_db_for_artwork_by_artist(self, name):
        database = SqliteDatabase(self.db)
        database.connect()
        # Locate all artwork with the corresponding name
        artwork_list = Artwork.select().where(Artwork.artist == name)
        # Display all artwork 
        database.close()
        return artwork_list


    def search_db_for_available_artwork_by_artist(self, name):
        database = SqliteDatabase(self.db)
        database.connect()
        # Locate all artwork with the corresponding name that is available
        artwork_list = Artwork.select().where(Artwork.artist == name, Artwork.available == True)
        # Display all available artwork 
        database.close()
        return artwork_list


    def add_new_artwork_to_db(self, name, name_of_artwork, price, available):
        database = SqliteDatabase(self.db)
        database.connect()  
        new_artwork = Artwork(artist=name, name_of_artwork=name_of_artwork, price=price, available=available)
        new_artwork.save()
        database.close()
        return new_artwork


    def delete_artwork_in_db(self, name_of_artwork):
        database = SqliteDatabase(self.db)
        database.connect()
        delete = Artwork.delete().where(Artwork.name_of_artwork == name_of_artwork).execute()
        database.close()
        return delete


    def db_change_artwork_availability(self, name_of_artwork, availability):
        database = SqliteDatabase(self.db)
        database.connect()
        updated_artwork = Artwork.update(available=availability).where(Artwork.name_of_artwork == name_of_artwork).execute()
        database.close()
        return updated_artwork


    def db_clear_tables(self):
        database = SqliteDatabase(self.db)
        database.connect()
        Artwork.delete().where(Artwork.name_of_artwork != '').execute()
        Artist.delete().where(Artist.name != '').execute()
        database.close()