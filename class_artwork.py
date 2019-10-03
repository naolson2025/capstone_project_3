from peewee import *
from class_artist import Artist

db = SqliteDatabase('artstore_db.sqlite')
#db = SqliteDatabase('test_artstore_db.sqlite')

# Create model class. 
class Artwork(Model):
    # use the artist name as the foreign key for each piece of artwork
    artist = ForeignKeyField(Artist, to_field="name")
    name_of_artwork = CharField()
    price = FloatField()
    available = BooleanField()

    # Link this model to the database
    class Meta:
        database = db

    def __str__(self):
        return f'Artist: {self.artist} \tArtwork Name: {self.name_of_artwork} \tPrice: {self.price} \tAvailable: {self.available}'