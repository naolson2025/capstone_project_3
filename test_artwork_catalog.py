from peewee import *
from main import *
import database
from unittest import TestCase
from class_artist import Artist
from class_artwork import Artwork


class TestArtworkCatalog(TestCase):

    test_db_url = 'test_artstore_db.sqlite'
    test_db = SqliteDatabase('test_artstore_db.sqlite')

    def setUp(self):
        database.db = self.test_db
        database.db.connect()
        database.db.create_tables([Artist])
        database.db.create_tables([Artwork])
        Artwork.delete().execute()
        Artist.delete().execute()
        database.db.close()


    def test_add_new_artist_to_db(self):
        add_new_artist_to_db('Bob', 'Bob@gmail.com')
        expected = {'Bob':'Bob@gmail.com'}
        self.compare_db_to_expected_artist_table(expected)


    def compare_db_to_expected_artist_table(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM Artist').fetchall()

        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            # Artist exists and email is correct
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

        conn.close()
