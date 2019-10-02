from peewee import *
from main import *
from database import *
from unittest import TestCase
from class_artist import Artist
from class_artwork import Artwork

test_db_url = 'test_artstore_db.sqlite'

class TestArtworkCatalog(TestCase):

    test_db_url = 'test_artstore_db.sqlite'

    def setUp(self):
        test_db = Database(test_db_url)
        test_db.db_clear_tables()


    def test_add_new_artist_to_db(self):
        test_db = Database(test_db_url)
        test_db.add_new_artist_to_db('Bob', 'Bob@gmail.com')
        expected = (1, 'Bob', 'Bob@gmail.com')
        self.compare_db_to_expected_artist_table(expected)


    def compare_db_to_expected_artist_table(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM Artist').fetchall()

        for row in all_data:
            print(row)
            print(expected)
            # ID, Artist, and email should all match
            self.assertEqual(row[0], expected[0])            
            self.assertEqual(row[1], expected[1])  
            self.assertEqual(row[2], expected[2])  

        conn.close()
