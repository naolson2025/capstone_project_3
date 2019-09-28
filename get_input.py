def get_artist_name():
    while True:
        name = input('Enter the name of the artist: ')
        if name != '':
            break
        else:
            print('Name cannot be blank.')
    return name


def get_artist_email():
    while True:
        email = input('Enter the email of the new artist: ')
        if email != '':
            break
        else:
            print('Email cannot be blank')
    return email


def get_name_of_artwork():
    while True:
        name_of_artwork = input('Enter the name of the piece of artwork: ')
        if name_of_artwork != '':
            break
        else:
            print('Name of artwork cannot be blank')
    return name_of_artwork


def get_price_of_artwork():
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
    return price


def get_artwork_availability():
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
    return availability

# if the artist is already in the db return true
# if not return false
def validate_artist_in_db(db_search_results):
    if len(db_search_results) > 0:
        return True
    else:
        return False