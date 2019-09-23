from peewee import *
import class_artist as Artist

db = SqliteDatabase('artstore_db.sqlite')

# Create model class. 
class Artwork(Model):
    # use the artist name as the foreign key for each piece of artwork
    artist = ForeignKeyField(Artist.Artist, to_field="name")
    name_of_artwork = CharField()
    price = FloatField()
    available = BooleanField()

    # Link this model to the database
    class Meta:
        database = db

    def __str__(self):
        return f'{self.artist} + "\t|\t" + {self.name_of_work} + "\t|\t" + {self.price} + "\t|\t" + {self.available}'