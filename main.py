import random

destinations_list = ["Germany", "Iceland", "Italy", "Norway", "Sweden"]
entertainments_list = ["Exploring", "Hiking", "Relaxing", "Shopping",]
transportations_list = ["Boat", "Plane", "Taxi", "Train"]
restaurants_list = ["Germanic", "Italian", "Scandinavian", "Local Favorite"]

def destinations_randomizer(destinations):
    destination_result = random.choice(destinations)
    return destination_result

def entertainments_randomizer(entertainments):
    entertainment_result = random.choice(entertainments)
    return entertainment_result

def transportations_randomizer(transportations):
    transportation_result = random.choice(transportations)
    return transportation_result

def restaurants_randomizer(restaurants):
    restaurant_result = random.choice(restaurants)
    return restaurant_result

def destination_confirmation(destinations):
    destination_result = destinations_randomizer(destinations)
    print("")
    print("We're sorry. How about " + destination_result + " ?")
    print("")
    destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
    if destination_choice == "Yes":
        return destination_result    
    else:
        destination_confirmation(destinations)
        
def entertainment_confirmation(entertainments_list):
    entertainment_result = entertainments_randomizer(entertainments_list)
    print("")
    print("We're sorry. How about " + entertainment_result + " ?")
    print("")
    entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
    if entertainment_choice == "Yes":
        return entertainment_result
    else:
        entertainment_confirmation(entertainments_list)

def transportation_confirmation(transportations_list):
    transportation_result = transportations_randomizer(transportations_list)
    print("")
    print("We're sorry. How about " + transportation_result + " ?")
    print("")
    transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
    if transportation_choice == "Yes":
        return transportation_result
    else:
        transportation_confirmation(transportations_list)

def restaurant_confirmation(restaurants_list):
    restaurant_result = restaurants_randomizer(restaurants_list)
    print("")
    print("We're sorry. How about " + restaurant_result + " ?")
    print("")
    restaurant_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
    if restaurant_choice == "Yes":
        return restaurant_result
    else:
        restaurant_confirmation(restaurants_list)

destination_result = destinations_randomizer(destinations_list)
entertainment_result = entertainments_randomizer(entertainments_list)
transportation_result = transportations_randomizer(transportations_list)
restaurant_result = restaurants_randomizer(restaurants_list)

print("")
print("Welcome to the devCodeCamp Day Trip Generator.")
print("")
print(f"We have selected {destination_result} as your destination.")
print("")
destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

def destination_choice_function(destination_choice):
    if destination_choice != "Yes":
        destination_result = destinations_randomizer(destinations_list)
        print("")
        print(f"We're sorry. How about {destination_result}?")
        print("")
        destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
        if destination_choice != "Yes":
            destination_choice_function(destination_choice)
        else:
            print("")
            print("Congratulations on choosing your destination. Let's move on.")
            print("")
    else:
        print("")
        print("Congratulations on choosing your destination. Let's move on.")
        print("")
destination_choice = destination_choice_function(destination_choice)

print("")
print("We have selected " + entertainment_result + " as your entertainment.")
print("")
entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

def entertainment_choice_function(entertainment_choice):
    if entertainment_choice != "Yes":
        entertainment_result = entertainments_randomizer(entertainments_list)
        print("")
        print(f"We're sorry. How about {entertainment_result}?")
        print("")
        entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
        if entertainment_choice != "Yes":
            entertainment_choice_function(entertainment_choice)
        else:
            print("")
            print("Congratulations on choosing your entertainment. Let's move on.")
            print("")    
    else:
        print("")
        print("Congratulations on choosing your entertainment. Let's move on.")
        print("")
entertainment_choice = entertainment_choice_function(entertainment_choice)

print("")
print("We have selected " + transportation_result + " as your transportation.")
print("")
transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

def transportation_choice_function(transportation_choice):
    if transportation_choice != "Yes":
        transportation_result = transportations_randomizer(transportations_list)
        print("")
        print("We're sorry. How about " + transportation_result + " ?")
        print("")
        transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
        if transportation_choice != "Yes":
            transportation_choice_function(transportation_choice)
        else:
            print("")
            print("Congratulations on choosing your transportation. Let's move on.")
            print("")   
    else:
        print("")
        print("Congratulations on choosing your transportation. Let's move on.")
        print("")
transportation_choice = transportation_choice_function(transportation_choice)

print("")
print("We have selected " + restaurant_result + " as your dining option.")
print("")
restaurant_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

def restaurant_choice_function(restaurant_choice):
    if restaurant_choice != "Yes":
        restaurant_result = restaurants_randomizer(restaurants_list)
        print("")
        print("We're sorry. How about " + restaurant_result + " ?")
        print("")
        restaurant_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")
        if restaurant_choice != "Yes":
            restaurant_choice_function(restaurant_choice)
        else:
            print("")
            print("Congratulations on choosing your dining option. Let's move on.")
            print("")   
    else:
        print("")
        print("Congratulations on choosing your dining option. Let's move on.")
        print("")
restaurant_choice = restaurant_choice_function(restaurant_choice)

print("")
print("Congratulations. We have completed generating your day trip.")
print("")
print("Now, let's confirm that this is the trip you want.")
print("")
print("Here is a summary of your trip:")
print(f"Destination: {destination_result}")
print(f"Entertainment: {entertainment_result}")
print(f"Transportation: {transportation_result}")
print(f"Restaurant: {restaurant_result}")
print("")

def user_confirmation_function(destination_result, entertainment_result, transportation_result, restaurant_result):
    user_confirmation = input("Type 'Yes' to confirm or 'No' to make changes. ")
    if user_confirmation == "No":
        print("")
        user_correction = input("Which option would you like to change?" \
            "Type '1' for Destination, '2' for Entertainment, '3' for Mode of transportation, or '4' for Restaurant. ")

        if user_correction == "1":
            destination_result = destinations_randomizer(destinations_list)
            print("")
            print("We have selected " + destination_result + " as your destination.")
            print("")
            destination_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

            if destination_choice != "Yes":
                destination_result = destination_confirmation(destinations_list)   
            else:
                print("")
                print("Congratulations on choosing your destination. Let's move on.")
                print("")
                return destination_result

        elif user_correction == "2":
            entertainment_result = entertainments_randomizer(entertainments_list)
            print("")
            print("We have selected " + entertainment_result + " as your entertainment.")
            print("")
            entertainment_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

            if entertainment_choice != "Yes":
                entertainment_result = entertainment_confirmation(entertainments_list)
            else:
                print("")
                print("Congratulations on choosing your entertainment. Let's move on.")
                print("")

        elif user_correction == "3":
            transportation_result = transportations_randomizer(transportations_list)
            print("")
            print("We have selected " + transportation_result + " as your transportation.")
            print("")
            transportation_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

            if transportation_choice != "Yes":
                transportation_result = transportation_confirmation(transportations_list)
            else:
                print("")
                print("Congratulations on choosing your transportation. Let's move on.")
                print("")

        elif user_correction == "4":
            restaurant_result = restaurants_randomizer(restaurants_list)
            print("")
            print("We have selected " + restaurant_result + " as your destination.")
            print("")
            restaurant_choice = input("Type 'Yes if you agree or 'No' if you disagree. ")

            if restaurant_choice != "Yes":
                restaurant_result = restaurant_confirmation(restaurants_list)
            else:
                print("")
                print("Congratulations on choosing your restaurant. Let's move on.")
                print("")

        print("")
        print("Congratulations. We have completed generating your day trip.")
        print("")
        print("Now, let's confirm that this is the trip you want.")
        print("")
        print("Here is a summary of your trip:")
        print("    Destination: " + destination_result)
        print("    Entertainment: " + entertainment_result)
        print("    Mode of transportation: " + transportation_result)
        print("    Restaurant: " + restaurant_result)
        print("")
        user_confirmation_function(destination_result, entertainment_result, transportation_result, restaurant_result)
    else:
        print("")
        print("Get ready for the adventure of a lifetime. You will be arriving in " + destination_result + " by " + transportation_result + " where you will spend the day " + entertainment_result + ". " + "You will end the day by enjoying a wonderful " + restaurant_result + " meal.")
        print("")
        print("Thank you for using the devCodeCamp Day Trip Planner")
        #return [destination_result, entertainment_result, transportation_result, restaurant_result]
confirmed_results = user_confirmation_function(destination_result, entertainment_result, transportation_result, restaurant_result)