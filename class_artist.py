from peewee import *

#db = SqliteDatabase('artstore_db.sqlite')
db = SqliteDatabase('test_artstore_db.sqlite')

# Create model class. 
class Artist(Model):
    name = CharField()
    email = CharField()

    # Link this model to the database
    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} \tEmail: {self.email}'