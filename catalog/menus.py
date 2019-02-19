#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurant.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create Dummy user
User1 = User(
    name="Chandu Siddartha",
    email="gsiddartha19@gmail.com",
    picture='https://lh5.googleusercontent.com/-8jCWuoDqb2I'
            '/AAAAAAAAAAI/AAAAAAAAAAc/m0qr01JjGFg/photo.jpg')
session.add(User1)
session.commit()

# Menu for Triple Spicy
restaurant1 = Restaurant(
    user_id=1,
    name="Triple Spicy",
    rating=5,
    cuisine='Indian')

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(
    user_id=1,
    name="Chicken Drumsticks",
    description="A Chicken Drumstick is the lower part of the chicken leg",
    price=2.5,
    restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(
    user_id=1,
    name="Chicken Chettinad",
    description="Chicken Chettinad or Chettinad chicken is a classic Indian"
                " recipe, from the cuisine of Chettinad",
    price=7.5,
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="Prawns Kuzhambu",
    description="Prawn is a common name for small aquatic crustaceans with an"
                " exoskeleton and ten legs, some of which can be eaten.",
    price=14,
    restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Roast chicken",
    description="Roast chicken is chicken prepared as food by roasting whether"
                " in a home kitchen, over a fire, or with a"
                " professional rotisserie.",
    price=15,
    restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(
    user_id=1,
    name="Triple-layer Carrot Cake",
    description="Moist layers of carrot cake with coconut and pecans topped"
                " with a sweet vanilla cream cheese icing.",
    price=5.19,
    restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Chinese Bowl
restaurant1 = Restaurant(
    user_id=1,
    name="Chinese Bowl",
    rating=3,
    cuisine='Chinese')

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(
    user_id=1,
    name="Kung Pao chicken",
    description="Kung Pao chicken, also transcribed as Gong Bao or Kung Po, is"
                " a spicy, stir-fried Chinese dish made with chicken,"
                " peanuts, vegetables, and chili peppers.",
    price=3,
    restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(
    user_id=1,
    name="Mapo doufu",
    description="Mapo doufu or mapo tofu is a popular Chinese dish from"
                " Sichuan province.",
    price=5.3,
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="Dumpling",
    description="Dumpling is a broad classification for a dish that consists"
                " of piece of dough wrapped around a filling or of"
                " dough with no filling.",
    price=2.19,
    restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Spring roll",
    description="Spring rolls are a large variety of filled, rolled appetizers"
                " or dim sum found in East Asian, South Asian, and"
                " Southeast Asian cuisine.",
    price=4.1,
    restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(
    user_id=1,
    name="Chow mein",
    description="Chow mein are Chinese stir-fried noodles, the name being the"
                " romanization of the Taishanese.",
    price=12,
    restaurant=restaurant1)

session.add(menuItem5)
session.commit()

# Menu for Outback Steakhouse
restaurant1 = Restaurant(
    user_id=1,
    name="Outback Steakhouse",
    rating=5,
    cuisine='American')

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(
    user_id=1,
    name="KOOKABURRA WINGS",
    description="30 chicken wings tossed in our secret spices served with our"
                " Blue Cheese dressing and celery.",
    price=25.9,
    restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(
    user_id=1,
    name="CHICKEN TENDER",
    description="15 crispy white-meat tenders served with choice of"
                " honey mustard or Buffalo sauce.",
    price=15.33,
    restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="RIBEYE",
    description="Well-marbled, juicy and savory. Wood-fire grilled with the"
                " natural flavor of oak.",
    price=19.5,
    restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="AYERS ROCK NY STRIP",
    description="NY Strip full of rich flavor. Seasoned and"
                " seared to perfection.",
    price=13.2,
    restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(
    user_id=1,
    name="MINI DESSERT PARFAITS",
    description="Layers of rich, creamy filling topped with whipped cream and"
                " served in an old-fashioned mini Mason jar.",
    price=12,
    restaurant=restaurant1)

session.add(menuItem5)
session.commit()

print "added menu items!"
