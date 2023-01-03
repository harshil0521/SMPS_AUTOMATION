def greet_user():
    print("Hello!")


greet_user()


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


def make_pizza(*toppings):
    print(toppings)


make_pizza('periperi', "cheese burst")

"""To change the name of the function"""
# from pizza import make_pizza as mp
"""    To import all function use *    """
# from pizza import *

