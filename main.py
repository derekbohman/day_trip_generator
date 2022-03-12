#This is going to be tough. You've got this.

import random
destinations = ["Iceland", "Italy", "New Zealand", "Norway"]
entertainments = ["Explore", "Museum", "Relax", "Show"]
mode_of_transportations = ["Boat", "Plane"]
restaurants = ["Italian", "Scandinavian", "Mexican", "Local Favorite"]

random_destination = random.choice(destinations)
random_entertainment = random.choice(entertainments)
random_mode_of_transportation = random.choice(mode_of_transportations)
random_restaurants = random.choice(restaurants)
destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
mode_of_transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

print("")
print("Welcome to the devCodeCamp Day Trip Generator. We have selected " + random_destination + " as your destination.")
print(destination_choice)

if destination_choice != "Yes":
    print("We're sorry. How about " + random_destination + " ?")
    print(destination_choice)
else:
    print("Congratulations on choosing your destination. Let's move on.")
