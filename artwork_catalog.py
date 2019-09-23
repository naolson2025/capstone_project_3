import sqlite3
from peewee import *
import class_artist as Artist
import class_artwork as Artwork

# Assign database
db = SqliteDatabase('artstore_db.sqlite')

# define the main method 
def main():
    createDataBase()
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
            addNewArtist()

        if user_choice == 2:
            searchArtworkByArtist()

        if user_choice == 3:
            searchAvailableArtworkByArtist()

        if user_choice == 4:
            addNewArtwork()

        if user_choice == 5:
            deleteArtwork()

        if user_choice == 6:
            changeArtworkAvailability()
            
        if user_choice == 7:
            break

def createDataBase():
    # Create the database connection to a db file
    db.connect()
    tables = db.get_tables()
    # If there are no tables in the db then add this base data
    if len(tables) == 0:
        db.create_tables([Artist.Artist])
        db.create_tables([Artwork.Artwork])

        # Add artists to the db
        elon = Artist.Artist(name='Elon Musk', email='elon.musk@gmail.com')
        elon.save()
        jeff = Artist.Artist(name='Jeff Bezos', email='jeff.bezos@gmail.com')
        jeff.save()
        joe = Artist.Artist(name='Joe Rogan', email='joe.rogan@gmail.com')
        joe.save()
        andrew = Artist.Artist(name='Andrew Yang', email='andrew.yang@gmail.com')
        andrew.save()

        # Add artwork to the db
        tesla_car = Artwork.Artwork(artist='Elon Musk', name_of_artwork='tesla_car', price=300.99, available=True)
        tesla_truck = Artwork.Artwork(artist='Elon Musk', name_of_artwork='tesla_truck', price=521.39, available=False)
        tesla_car.save()
        tesla_truck.save()

        fire_stick = Artwork.Artwork(artist='Jeff Bezos', name_of_artwork='fire_stick', price=152.78, available=True)
        fire_phone = Artwork.Artwork(artist='Jeff Bezos', name_of_artwork='fire_phone', price=772.78, available=False)
        fire_stick.save()
        fire_phone.save()

        chimp = Artwork.Artwork(artist='Joe Rogan', name_of_artwork='chimp', price=22.88, available=True)
        gorilla = Artwork.Artwork(artist='Joe Rogan', name_of_artwork='gorilla', price=33.88, available=False)
        chimp.save()
        gorilla.save()

        ubi = Artwork.Artwork(artist='Andrew Yang', name_of_artwork='ubi', price=12000, available=True)
        climate_protection = Artwork.Artwork(artist='Andrew Yang', name_of_artwork='climate_protection', price=5000, available=False)
        ubi.save()
        climate_protection.save()
 
    db.close()

# Menu method will print all the progam options
def menu():
    print('1. Add a new artist')
    print('2. Search all artwork by an artist')
    print('3. Search all available artwork for an artist')
    print('4. Add a new piece of artwork')
    print('5. Delete a piece of artwork')
    print('6. Change the availability of a piece of artwork')
    print('7. Exit program')

def addNewArtist():
    db.connect()
    # Get the name and email of the new artist
    name = input('Enter the name of the new artist: ')
    email = input('Enter the email of the new artist: ')
    # Add the new artist to the db
    new_artist = Artist.Artist(name=name, email=email)
    new_artist.save()
    print(name + ' was added successfully.')
    db.close()

def searchArtworkByArtist():
    db.connect()
    # Get the name of the artist that the user wants to view their artwork
    name = input('Enter the name of the artist: ')
    # Locate all artwork with the corresponding name
    artwork_list = Artwork.Artwork.select().where(Artwork.Artwork.artist == name)
    # Display all artwork 
    if len(artwork_list) == 0:
        print('This artist has no artwork in the database.')
    else:
        for artwork in artwork_list:
            print(artwork)
    db.close()

def searchAvailableArtworkByArtist():
    db.connect()
    # Get the name of the artist that the user wants to view their available artwork
    name = input('Enter the name of the artist: ')
    # Locate all artwork with the corresponding name that is available
    artwork_list = Artwork.Artwork.select().where(Artwork.Artwork.artist == name, Artwork.Artwork.available == True)
    # Display all available artwork 
    # Test if there is no available artwork
    if len(artwork_list) == 0:
        print('This artist has no available artwork.')
    else:
        for artwork in artwork_list:
            print(artwork)
    db.close()

def addNewArtwork():
    db.connect()
    # Get the name of the artist that the user wants to view their artwork
    name = input('Enter the name of the artist: ')
    name_of_artwork = input('Enter the name of the piece of artwork: ')   
    # loop to make sure the number of catches is a positive number
    while True:
        try:
            price = float(input('Enter the price of the piece of artwork: '))
            if price > 0:
                break
            else:
                print('Price must be a positive number.')
        except:
            pass
        print('Price must be a number.')
    # Loop to get the user to enter true or false for artwork availability
    while True:
        try:
            available = bool(input('Is this artwork available? True or False: '))
            break
        except:
            pass
        print('Entry invalid.')

    new_artwork = Artwork.Artwork(artist=name, name_of_artwork=name_of_artwork, price=price, available=available)
    new_artwork.save()
    db.close()

def deleteArtwork():
    db.connect()
    # Get the name of the artwork
    name_of_artwork = input('Enter the name of the artwork you want to delete: ')
    delete = Artwork.Artwork.delete().where(Artwork.Artwork.name_of_artwork == name_of_artwork).execute()
    if delete > 0:
        print(name_of_artwork + " was deleted from the database.")
    else:
        print('This piece of artwork was not found in the database.')
    db.close()

def changeArtworkAvailability():
    db.connect()
    # Get the name of the artwork
    name_of_artwork = input('Enter the name of the artwork that\'s availability is being changed: ')
    # Loop to get the user to enter true or false for artwork availability
    while True:
        availability = input('Is this artwork available? Y or N: ')
        if availability.lower() == 'y':
            availability = True
            break
        elif availability.lower() == 'n':
            availability = False
            break
        else:
            pass
            print('Entry invalid.')
    update = Artwork.Artwork.update(available=availability).where(Artwork.Artwork.name_of_artwork == name_of_artwork).execute()
    if update > 0:
        print(name_of_artwork + ' now has the availability of: ' + str(availability))
    else:
        print('This piece of artwork was not found in the database.') 
    db.close()

main()