import sqlite3
from peewee import *
from class_artist import Artist
from class_artwork import Artwork
from database import *
from get_input import *
from display import *

db_file = 'artstore_db.sqlite'

# define the main method 
def main():
    database = Database(db_file)
    print('This program manages a database of artists and thier artwork')
    print('Enter the number of the option you want to choose.\n')
    # This loop will continue until the user enters 6 to exit the progam
    while True:
        # print user options
        print()
        menu()
        print()

        # The program will test that the user's input is one of the 6 options by comparing it to the list of choices  
        while True:
            try:
                choices = [1, 2, 3, 4, 5, 6, 7]
                user_choice = int(input('> '))
                if user_choice in choices:
                    break
            except:
                pass
            print('A number 1-7 must be selected.\n')

        if user_choice == 1:
            name = get_artist_name()
            email = get_artist_email()
            add_new_artist(name, email)

        if user_choice == 2:
            name = get_artist_name()
            search_artwork_by_artist(name)

        if user_choice == 3:
            name = get_artist_name()
            search_available_artwork_by_artist(name)

        if user_choice == 4:
            name = get_artist_name()
            artwork_name = get_name_of_artwork()
            artwork_price = get_price_of_artwork()
            artwork_availability = get_artwork_availability()
            add_new_artwork(name, artwork_name, artwork_price, artwork_availability)

        if user_choice == 5:
            artwork_name = get_name_of_artwork()
            delete_artwork(artwork_name)

        if user_choice == 6:
            name = get_name_of_artwork()
            change_artwork_availability(name)
            
        if user_choice == 7:
            break


def add_new_artist(name, email):
    database = Database(db_file)
    # Add the new artist to the db
    new_artist = database.add_new_artist_to_db(name, email)
    display_new_artist(new_artist)


def search_artwork_by_artist(name):
    database = Database(db_file)
    artwork_list = database.search_db_for_artwork_by_artist(name)
    display_artwork_by_an_artist(artwork_list)

 
def search_available_artwork_by_artist(name):
    database = Database(db_file)
    artwork_list = database.search_db_for_available_artwork_by_artist(name)
    display_available_artwork_by_an_artist(artwork_list)


def add_new_artwork(name, name_of_artwork, price, available):
    database = Database(db_file)
    db_search_results = database.db_search_for_artist(name)
    is_artist_in_db = validate_artist_in_db(db_search_results)
    if is_artist_in_db == False:
        email = get_artist_email()
        add_new_artist(name, email)
    new_artwork = database.add_new_artwork_to_db(name, name_of_artwork, price, available)
    display_new_artwork(new_artwork)


def delete_artwork(name_of_artwork):
    database = Database(db_file)
    delete = database.delete_artwork_in_db(name_of_artwork)
    display_deleted(delete, name_of_artwork)


def change_artwork_availability(name_of_artwork):
    database = Database(db_file)
    availability = get_artwork_availability()
    updated_artwork = database.db_change_artwork_availability(name_of_artwork, availability)
    display_change_artwork_availability(name_of_artwork, updated_artwork, availability)


if __name__=='__main__':
    main()