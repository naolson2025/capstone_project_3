from peewee import *
from main import *
from database import *
from unittest import TestCase
from class_artist import Artist
from class_artwork import Artwork

# Testing assumes the test database is linked to the Artist and Artwork classes

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

    def test_db_search_for_artist(self):
        test_db = Database(test_db_url)
        test_db.add_new_artist_to_db('Steve', 'Steve@gmail.com')
        artist = test_db.db_search_for_artist('Steve')
        self.assertEqual('Steve', artist)

    def test_add_new_artwork_to_db(self):
        test_db = Database(test_db_url)
        test_db.add_new_artist_to_db('Tim', 'Tim@gmail.com')
        test_db.add_new_artwork_to_db('Tim', 'Apple', 200.00, True)
        expected = ['Tim', 'Apple', 200.00, True]
        self.compare_db_to_expected_artwork_table(expected)

    def test_search_db_for_artwork_by_artist(self):
        test_db = Database(test_db_url)
        test_db.add_new_artist_to_db('Jim', 'Jim@gmail.com')
        test_db.add_new_artwork_to_db('Jim', 'Panda', 100.00, True)
        artwork_list = test_db.search_db_for_artwork_by_artist('Jim')
        expected = ['Jim', 'Panda', 100.00, True]
        self.assertEqual(expected, artwork_list)

    def compare_db_to_expected_artist_table(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM Artist').fetchall()

        for row in all_data:
            # ID, Artist, and email should all match
            #self.assertEqual(row[0], expected[0])            
            #self.assertEqual(row[1], expected[1])  
            #self.assertEqual(row[2], expected[2])  
            for item in row:
                self.assertEqual(row[item], expected[item])

        conn.close()

    def compare_db_to_expected_artwork_table(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM Artwork').fetchall()

        for row in all_data:
            # ID, Artist, and email should all match
            #self.assertEqual(row[0], expected[0])            
            #self.assertEqual(row[1], expected[1])  
            #self.assertEqual(row[2], expected[2])  
            for item in row:
                self.assertEqual(row[item], expected[item])

        conn.close()
