#This is going to be tough. You've got this.

import random

destinations = ["Germany", "Iceland", "Italy", "Norway", "Sweden"]
entertainments = ["Exploring", "Hiking", "Relaxing", "Shopping",]
modes_of_transportation = ["Boat", "Plane", "Taxi", "Train"]
restaurants = ["Germanic", "Italian", "Scandinavian", "Local Favorite"]

def destinations_randomizer(destinations):
    destination_result = random.choice(destinations)
    return destination_result

def entertainments_randomizer(entertainments):
    entertainment_result = random.choice(entertainments)
    return entertainment_result

def modes_of_transportation_randomizer(modes_of_transportation):
    mode_of_transportation_result = random.choice(modes_of_transportation)
    return mode_of_transportation_result

def restaurants_randomizer(restaurants):
    restaurant_result = random.choice(restaurants)
    return restaurant_result

destination_result = destinations_randomizer(destinations)
entertainment_result = entertainments_randomizer(entertainments)
mode_of_transportation_result = modes_of_transportation_randomizer(modes_of_transportation)
restaurant_result = restaurants_randomizer(restaurants)

print("")
print("Welcome to the devCodeCamp Day Trip Generator. We have selected " + destination_result + " as your destination.")
print("")
destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

while destination_choice != "Yes":
    destination_result = destinations_randomizer(destinations)
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
    entertainment_result = entertainments_randomizer(entertainments)
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
    mode_of_transportation_result = modes_of_transportation_randomizer(modes_of_transportation)
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
    restaurant_choice = restaurants_randomizer(restaurants)
    print("")
    print("We're sorry. How about " + restaurant_result + " ?")
    print("")
    restaurant_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
else:
    print("")
    print("Congratulations on choosing your dining option. Let's move on.")
    print("")

print("")
print("Congratulations. We have completed generating your day trip.")
print("")
print("Now, let's confirm that this is the trip you want.")
print("")
print("The trip that we have generated for you is:")
print("Destination: " + destination_result)
print("Entertainment: " + entertainment_result)
print("Mode of transportation: " + mode_of_transportation_result)
print("Restaurant: " + restaurant_result)
print("")

user_confirmation = input("Type 'Yes' to confirm or 'No' to make changes.")

if user_confirmation == "Yes":
    print("Get ready for the adventure of a lifetime. You will be arriving in " + destination_result + \
    " by " + mode_of_transportation_result + " where you will spend the day " + entertainment_result + ". " + \
    "You will end the day by enjoying a wonderful " + restaurant_result + " meal.")
else:
    print("We apologize, but that's what's happening. Have fun!")