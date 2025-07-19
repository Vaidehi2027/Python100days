# def drink_potion():
#   potion_strength = 2
#   print(f"THe value of potion {potion_strength}")
# drink_potion()
# print(potion_strength)  

#GLOBAL SCOPE

# player_health = 10
#THIS IS  A GLOBAL VARIBLAE SO WE CAN ACCESS IT THROUGH ANY FUNCTION
# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#     print(player_health)
#   drink_potion()
# print(player_health)

#THERE IS NO BLOCK SCOPE
# game_level = 3
# def create_enemy():
#     enemies = ['Skeleton',"Zombie","Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)
# create_enemy()
#THE SCOPE IS ONLY RESYRUCTED TO  DEFINING THE FUNCTION 
#IF U CREATE A VARIABLE IN A FUNCTION THEN IT IS ACCESSIBLE IN THAT FUNCTION ONLY IF,WHILE,FOR DOES NOT COUNT AS CREARING A LOCAL SCOPE

#MODIFYING GLOBAL SCOPE
#HOW TO CHANGE A GLOBAL INTO THE LOCAL SCOPE
# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"Enemies outside function: {enemies}")
# 22211059
# 22211455

# enemies = 1
# def increase_enemies():
#     """It is a function"""
#     print(f"Enemies inside function : {enemies}")
#     return enemies + 1
#     # THIS IS THE CODE TO INCREASE THE ENEMIES AND WITHOUT MODIFYING THE GLOBAL VARIABLE

# enemies = increase_enemies()
# print(f"Enemies outside function: {enemies}")

#GLOBAL CONSTANTS
# PI = 3.14159
# def calc():
#     print(PI)
# calc()
# TO DIFFERENTIATE VARIABLES FROM CONSTANTS ALL THE GLOBAL CONSTANTS ARE UPPER CASED

#FINAL PROJECT
#NUMBER GUESSING NAME
# from random import *
# from art import logo
# print(logo)
# print("Welcome to the number guessing game")

# print("I am thinking of a number 1 and 100!")
# should_continue = True
# while should_continue():
#     number_1 = randint(1,100)
#     no_of_chances = 0
#     difficulty = input("Choose a difficulty: 'easy' or 'hard': ")
#     if difficulty == 'easy':
#         no_of_chances = 10
#     elif difficulty == 'hard':
#         no_of_chances = 5
#     for i in range(0,no_of_chances):
#         number_2 = int(input("Guess a number: "))
#         if number_1 == number_2:
#             print("Omg! You have cracked the number")
#             should_continue = False
#         elif number_1 > number_2:
#             print("Too low!")
#             print("Guess again!")
#         elif number_1 < number_2:
#             print("Too high!")
#             print("Guess again!")

#FINAL CODE
#CREATING A GLOBAL CONSTANTS
# BY ALL IN CAPAS WE ARE CREATING A GLOBAL CONSTANT
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#FUNCTION TO CHECK USER'S GUESS AGAINST ACTUAL ANSWER
from random import *
from art import logo
def check_answer(guess,answer,turns):
    """ checks answer against guess.Returns the number of turns remaining!"""
    if guess>answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it!The answer is {answer}")

# MAKE FUNCTION TO SET DIFFICULTY
def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#CHOOSING A RANDOM NUMBER
def game():
    answer = randint(1,100)
    print(logo)
    print("Welcome to guessing game")
    print("I'm thinking of a number between 1 and 100")

    turns = set_difficulty()

    #LET THE USER GUESS A NUMBER
    #DEFINING GUESS AS A GLOBAL VARIABLE
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number!")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess,answer,turns)
        
        if turns == 0:
            print("You have run out of guesses, you lose!")
            return
            #WE CAN USE RETURN KEYWORD TO END THE FUNCTION TOO 
        elif guess != answer:
            print("Guess again!")

    #TRACK THE NUMBER OF TURNS AND REDUCE BY 1 IF THEY GET WRONG
    #REPEAT THE GUESSING FUNCTIONALITY IF THEY GET IT WRONG
game()

        






