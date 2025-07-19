#DICTIONARIES
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# student_grades["Harry"] = 81
# student_grades["Ron"] = 78
# student_grades["Hermione"] = 99
# student_grades["Draco"] = 74
# student_grades["Nevielle"] = 62

# # 🚨 Don't change the code below 👇
# print(student_grades)

# first_dictionary = {
#     "rob" : 93,
#     "harry" : 45,
#     "siva" : 56,
# }
#RETRIEVING ITEMS FROM DICTIONARY
# print(first_dictionary["rob"]) 
# list elements have to be acesses by the keys they are unordered so they cant be accessed using index

#ADDING NEW ITEMS TO DICTIONARY
# first_dictionary["mary"] = 45
# print(first_dictionary)

#CREATING AN EMPTY DICTIONARY
# empty_dictionary = {}

#WIPING A DICTIONARY
# first_dictionary = {}
# by this line we assign an empty dictionary to the existing dictionary and it wipes out the initial content
# print(first_dictionary)

#EDIT AN ITEM IN A DICTIONARY
# first_dictionary["rob"] = 56
# print(first_dictionary)

#looping through a dictionary
# for key in first_dictionary:
#     print(key)  
# Gives the keys in the dictionary
    # print(first_dictionary[key]) 
# Gives the values of the keys in the dictionary     


# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades={}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#   score = student_scores[key]
#   if score>90:
#     student_grades[key] = "Outstanding"
#   elif score>80:
#     student_grades[key] = "Exceeds Expectations"
#   elif score>70:
#     student_grades[key] = "Acceptable"
#   else:
#     student_grades[key]= "Fail"
  
# 🚨 Don't change the code below 👇
# print(student_grades)
#  Scores 91 - 100: Grade = "Outstanding"

# > Scores 81 - 90: Grade = "Exceeds Expectations"

# > Scores 71 - 80: Grade = "Acceptable"

# > Scores 70 or lower: Grade = "Fail"
# travel_log = {
# "Paris": {"cities_visited":["Paris","Lille","Dijon"],"total_visits":5},
# "Germany":{"cities_visited":["Dumdum","Chamcham","Chunchun"],"total_visits":6}}                      
# NESTING A DICTIONARY IN A DICTIONARY AND A LIST

#NESTING A DICTIONARY IN A LIST
# travel_log = [
#     {
#         "country":"Paris",
#         "cities_visited":["Paris","Lille","Dijon"],
#         "total_visits":5
#     },
#     {
#         "country":"Germany",
#         "cities_visited":["Dumdum","Chamcham","Chunchun"],
#         "total_visits":6
#     },
# ] 
# print(travel_log[0])

# nesting exercise
# def add_new_country(Country,no_of_visits,cities):
#   new_element = {}
#   new_element["country"] = Country
#   new_element["visits"] = no_of_visits
#   new_element["cities"] = Cities
#   travel_log.append(new_element)
# Country = input("Name the country you visited: ")
# no_of_visits = input("The no of visits u did: ")
# name = input("The names of cities you visited: ")
# Cities = name.split(',')
  
  
  
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# from replit import clear
# #HINT: You can call clear() to clear the output in the console.
# from art import logo
# print(logo)
# print("Hey bider,lets have a bid today!!")

# Response = True
# while Response:
#   name = input("Hello,whats your name? ")
#   bid = input("Whats your bid? $")
#   no_biders = input("Are there any other biders? ").lower()
#   Biders = {}
#   Biders[name] = bid
#   # print(Biders)
 
  
#   def game_of_thrones():
#     key_values = list(Biders.keys())
#     Values = list(Biders.values())
#     winning_bid = max(Values)
#     position = Values.index(winning_bid)
#     winner = key_values[position]
#     print(f"The winner is {winner} with a bid of {winning_bid} $")
    
#   if no_biders == "no":
#     Response = False
#     print("Lets stop bidding!")
#     game_of_thrones()
#   elif no_biders == "yes":
#     clear()

# ANOTHER WAY OF THE CODE(TRAINERS WAY)  
# from replit import clear
#HINT: You can call clear() to clear the output in the console.
# from art import logo
# print(logo)
# print("Hey bider,lets have a bid today!!")

# Response = True
# while Response:
#   name = input("Hello,whats your name? ")
#   bid = int(input("Whats your bid? $"))
#   no_biders = input("Are there any other biders? ").lower()
#   Biders = {}
#   Biders[name] = bid
#   # print(Biders)
#   def find_heighest_bid(biding_record):
#     winner = ''
#     heighest_bid = 0
#     for bidder in biding_record:
#       bid_amount = biding_record[bidder]
#       if bid_amount > heighest_bid:
#         heighest_bid = bid_amount
#         winner = bidder
#     print(f"The winner is {winner} with a bid of {heighest_bid}$")
    
#   if no_biders == "no":
#     Response = False
#     print("Lets stop bidding!")
#     find_heighest_bid(Biders)
#   elif no_biders == "yes":
#     clear()
  

    
