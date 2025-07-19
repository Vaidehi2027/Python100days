#HIGHER OR LOWER GAME

# DISPLAY ART
# from art import logo,vs
# # from game_data import data
# import random
# # from replit import clear
# print(logo)
# score = 0
# game_should_continue = True
# def format_data(account):
#   """Takes the account data and returns the printable format!"""
#   account_name = account["name"]
#   account_descr = account["description"]
#   account_country = account["country"]
#   return f"{account_name}, a {account_descr}, from {account_country}"

# def check_answer(guess,a_followers,b_followers):
#   """Take the user guess and follower counts and returns if they got it right"""
#   # if a_followers > b_followers:
#   #   if guess == "a":
#   #     return True
#   #   else:
#   #     return False
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"
#   #BASICALLY IT CHECKS IF THE USER HAS GUESSED IT RIGHT OR NOT IF THEY GUESSED IT RIGHT IT WILL RETURN TRUE OTHERWISE FASLSE
  
# # GENERATE A RANDOM ACCOUNT
# # account_b = random.choice(data)
# while game_should_continue:
#   account_a = account_b
# #   account_b = random.choice(data)
#   # WILL ONLY RUN IF THEY ARE DIFFERENT
#   while account_a == account_b:
#     # account_b = random.choice(data)
#   #REGENERATE THE B ONE IF THEY ARE SAME
  
#   # HOW TO FORMAT THE ACCOUNT DATA
  
#   print(f"Compare A:{format_data(account_a)}")
#   print(vs)
#   print(f"Against B:{format_data(account_b)}")
  
#   #ASK THE USER FOR A GUESS
#   guess = input('Who has more followers "A" or "B"?').lower()
  
#   #CHECK IF USER IS CORRECT
#   a_follower_count = account_a["follower_count"]
#   b_follower_count = account_b["follower_count"]
#   is_correct = check_answer(guess,a_follower_count,b_follower_count)
  
#   # CLEAR THE SCREEN
#   clear()
#   print(logo)
#   #GIVE USER FEEDBACK
#   if is_correct:
#     score += 1
#     print(f"You are right, user! Current score : {score}")
#   else:
#     game_should_continue = False
#     print(f"Sorry thats wrong! Final score: {score}")
#   #MAKING THE GAME REPEATABLE
#   # MAKING HTE ACCOUNTS AT POS B BECOME THE NEXT AT A
  