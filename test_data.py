from class_artist import Artist
from class_artwork import Artwork

def add_test_data():
    # Put into a separate function
    # Add artists to the db
    elon = Artist(name='Elon Musk', email='elon.musk@gmail.com')
    elon.save()
    jeff = Artist(name='Jeff Bezos', email='jeff.bezos@gmail.com')
    jeff.save()
    joe = Artist(name='Joe Rogan', email='joe.rogan@gmail.com')
    joe.save()
    andrew = Artist(name='Andrew Yang', email='andrew.yang@gmail.com')
    andrew.save()

    # Add artwork to the db
    tesla_car = Artwork(artist='Elon Musk', name_of_artwork='tesla_car', price=300.99, available=True)
    tesla_truck = Artwork(artist='Elon Musk', name_of_artwork='tesla_truck', price=521.39, available=False)
    tesla_car.save()
    tesla_truck.save()

    fire_stick = Artwork(artist='Jeff Bezos', name_of_artwork='fire_stick', price=152.78, available=True)
    fire_phone = Artwork(artist='Jeff Bezos', name_of_artwork='fire_phone', price=772.78, available=False)
    fire_stick.save()
    fire_phone.save()

    chimp = Artwork(artist='Joe Rogan', name_of_artwork='chimp', price=22.88, available=True)
    gorilla = Artwork(artist='Joe Rogan', name_of_artwork='gorilla', price=33.88, available=False)
    chimp.save()
    gorilla.save()

    ubi = Artwork(artist='Andrew Yang', name_of_artwork='ubi', price=12000, available=True)
    climate_protection = Artwork(artist='Andrew Yang', name_of_artwork='climate_protection', price=5000, available=False)
    ubi.save()
    climate_protection.save()