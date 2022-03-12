#This is going to be tough. You've got this.

from platform import java_ver
import random

destinations = ["Germany", "Iceland", "Italy", "Norway", "Sweden"]
entertainments = ["Hike", "Museum", "Relax", "Shop", "Theater"]
modes_of_transportations = ["Boat", "Plane", "Taxi", "Train", "Walk"]
restaurants = ["Germanic", "Italian", "Scandinavian", "Local Favorite"]

def destination_randomizer(destinations):
    destination_result = random.choice(destinations)
    return destination_result

def entertainment_randomizer(entertainments):
    entertainment_result = random.choice(entertainments)
    return entertainment_result

def mode_of_transportation_randomizer(modes_of_transportation):
    mode_of_transportation_result = random.choice(modes_of_transportation)
    return mode_of_transportation_result

def restaurants_randomizer(restaurants):
    restaurant_result = random.choice(restaurants)
    return restaurant_result

destination_result = destination_randomizer(destinations)
entertainment_result = entertainment_randomizer(entertainments)
mode_of_transportation_result = mode_of_transportation_randomizer(modes_of_transportations)
restaurant_result = restaurants_randomizer(restaurants)

print("")
print("Welcome to the devCodeCamp Day Trip Generator. We have selected " + destination_result + " as your destination.")
print("")
destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

while destination_choice != "Yes":
    destination_result = destination_randomizer(destinations)
    print("")
    print("We're sorry. How about " + destination_result + " ?")
    print("")
    destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
else:
    print("")
    print("Congratulations on choosing your destination. Let's move on.")
    print("")

print("")
print("We have selected " + entertainment_result + " as your entertainment.")
print("")
entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

while entertainment_choice != "Yes":
    print("")
    print("We're sorry. How about " + entertainment_result + " ?")
    print("")
    entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
else:
    print("")
    print("Congratulations on choosing your entertainment. Let's move on.")
    print("")

print("")
print("We have selected " + mode_of_transportation_result + " as your mode of transportation.")
print("")
mode_of_transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

while mode_of_transportation_choice != "Yes":
    print("")
    print("We're sorry. How about " + mode_of_transportation_result + " ?")
    print("")
    mode_of_transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
else:
    print("")
    print("Congratulations on choosing your mode of transportation. Let's move on.")
    print("")

print("")
print("We have selected " + restaurant_result + " as your dining option.")
print("")
restaurant_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

while restaurant_choice != "Yes":
    print("")
    print("We're sorry. How about " + restaurant_result + " ?")
    print("")
    restaurant_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
else:
    print("")
    print("Congratulations on choosing your dining option. Let's move on.")
    print("")