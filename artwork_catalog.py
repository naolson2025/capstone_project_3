import sqlite3
from peewee import *
from class_artist import Artist
from class_artwork import Artwork
from artwork_db import *
from get_input import *

# define the main method 
def main():
    create_data_base()
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


# Menu method will print all the progam options
def menu():
    print('1. Add a new artist')
    print('2. Search all artwork by an artist')
    print('3. Search all available artwork for an artist')
    print('4. Add a new piece of artwork')
    print('5. Delete a piece of artwork')
    print('6. Change the availability of a piece of artwork')
    print('7. Exit program')


def add_new_artist(name, email):
    # Add the new artist to the db
    add_new_artist_to_db(name, email)
    print(name + ' was added successfully.')


def search_artwork_by_artist(name):
    artwork_list = search_db_for_artwork_by_artist(name)
    display_artwork_by_an_artist(artwork_list)


def display_artwork_by_an_artist(artwork_list):
    if len(artwork_list) == 0:
        print('This artist has no artwork in the database.')
    else:
        for artwork in artwork_list:
            print(artwork)


def search_available_artwork_by_artist(name):
    db.connect()
    # Locate all artwork with the corresponding name that is available
    artwork_list = Artwork.Artwork.select().where(Artwork.Artwork.artist == name, Artwork.Artwork.available == True)
    # Display all available artwork 
    db.close()
    display_artwork_by_an_artist(artwork_list)


def add_new_artwork(name, name_of_artwork, price, available):
    db.connect()  
    new_artwork = Artwork.Artwork(artist=name, name_of_artwork=name_of_artwork, price=price, available=available)
    new_artwork.save()
    db.close()


def display_deleted(deleted):
    if deleted > 0:
        print("Artwork was deleted from the database.")
    else:
        print('This piece of artwork was not found in the database.')

def delete_artwork(name_of_artwork):
    db.connect()
    delete = Artwork.Artwork.delete().where(Artwork.Artwork.name_of_artwork == name_of_artwork).execute()
    db.close()
    display_deleted(delete)


def change_artwork_availability(name_of_artwork):
    db.connect()
    update = Artwork.Artwork.update(available=availability).where(Artwork.Artwork.name_of_artwork == name_of_artwork).execute()
    if update > 0:
        print(name_of_artwork + ' now has the availability of: ' + str(availability))
    else:
        print('This piece of artwork was not found in the database.') 
    db.close()

main()