# Menu method will print all the progam options
def menu():
    print('1. Add a new artist')
    print('2. Search all artwork by an artist')
    print('3. Search all available artwork for an artist')
    print('4. Add a new piece of artwork')
    print('5. Delete a piece of artwork')
    print('6. Change the availability of a piece of artwork')
    print('7. Exit program')


def display_new_artist(new_artist):
    print(new_artist.name + ' was added to the database.')


def display_artwork_by_an_artist(artwork_list):
    if len(artwork_list) == 0:
        print('This artist has no artwork in the database.')
    else:
        for artwork in artwork_list:
            print(artwork)


def display_available_artwork_by_an_artist(artwork_list):
    if len(artwork_list) == 0:
        print('This artist has no available artwork in the database.')
    else:
        for artwork in artwork_list:
            print(artwork)


def display_new_artwork(new_artwork):
    print(new_artwork)


def display_deleted(deleted, name_of_artwork):
    if deleted > 0:
        print(name_of_artwork + "  was deleted from the database.")
    else:
        print(name_of_artwork + ' was not found in the database.')


def display_change_artwork_availability(name_of_artwork, changed_artwork, availability):
    if changed_artwork > 0:
        print(name_of_artwork + ' now has the availability of: ' + str(availability))
    else:
        print('This piece of artwork was not found in the database.') 