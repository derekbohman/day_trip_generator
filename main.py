#This is going to be tough. You've got this.

import random

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

destinations = ["Iceland", "Italy", "New Zealand", "Norway"]
entertainments = ["Explore", "Museum", "Relax", "Show"]
modes_of_transportations = ["Boat", "Plane"]
restaurants = ["Italian", "Scandinavian", "Mexican", "Local Favorite"]

mode_of_transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

print("")
print("Welcome to the devCodeCamp Day Trip Generator. We have selected " + destination_randomizer + " as your destination.")
print("")
destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

if destination_choice != "Yes":
    print("We're sorry. How about " + destination_randomizer + " ?")
    destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
else:
    print("Congratulations on choosing your destination. Let's move on.")

print("")
print("We have selected " + entertainment_randomizer + " as your entertainment.")
print("")
entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

if entertainment_choice != "Yes":
    print("We're sorry. How about " + entertainment_randomizer + " ?")
    entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
else:
    print("Congratulations on choosing your entertainment. Let's move on.")