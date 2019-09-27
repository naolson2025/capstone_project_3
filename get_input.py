def get_artist_name():
    name = input('Enter the name of the new artist: ')
    return name


def get_artist_email():
    email = input('Enter the email of the new artist: ')
    return email


def get_name_of_artwork():
    name_of_artwork = input('Enter the name of the piece of artwork: ')
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