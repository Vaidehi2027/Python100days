import random
'''random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

#printing numbers from [1,5)
random5 = random_float * 5
print(random5)

# Randomising love calculator
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")'''

# Tails or head calculator
'''tails_random = random.randint(0,1)
if tails_random == 1:
    print("Heads, u have got a Heads")
elif tails_random == 0:
    print("Tails, you have got a Tails")'''

#LISTS
#Lists are a data structures in python which can hold any type of data
#States_of_America = ["Delaware","Pennsylvania","New Jersey"]
#lists let you store realted data and xan be stored in an order
'''print(States_of_America[0])
print(States_of_America[-1])
States_of_America[1] = "Pencil"
print(States_of_America)
States_of_America.append("Angelaland")
print(States_of_America)

States_of_America.extend(["Angelaland","Jack Beiber Land"])
print(States_of_America)'''

#Banker roulette
'''name_string = input("Give me the names of all friends separated by commas:\n")
name = name_string.split(', ')
print(name)
bill_payer = random.randint(0,len(name)-1)
print(bill_payer)
i = 0
if bill_payer == i:
    print(f"{name[i]}, has to pay for the meal today!")
person_who_will_pay = random.choice(name)
print(person_who_will_pay + " , is going to buy the meal today!")'''

'''Fruits = ["Apple",'Banana',"Mango","Kiwi"]
Vegetables= ["Lady finger","Cabbage","Tomato"]
My_basket = [Fruits,Vegetables]
print(My_basket)'''

#TRESURE GAME
'''row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do u want to put the treasure?")
horizontal= int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}")'''

'''fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])'''
Rock ='''
      _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
'''User_input = int(input("What do you want to choose? Type 0 for Rock,1 for paper and 2 for scissors\n"))
Games = [Rock,Paper,Scissors]
random_choice = random.randint(0,2)
computer_choice = Games[random_choice]'''
'''User = ""
if User_input == 0:
    User = Rock
elif User_input == 1:
    User = Paper
elif User_input == 2:
    User = Scissors'''

'''if User_input == 0 and computer_choice == Rock:
    print("There is a draw! Try again")
elif User_input == 1 and computer_choice == Paper:
    print("There is a draw! Try again")
elif User_input == 2 and computer_choice == Scissors:
    print("There is a draw! Try again")
elif User_input == 0 and computer_choice == Scissors:
    print("You won,user!")
elif User_input == 2 and computer_choice == Paper:
    print("You won,user!")
elif User_input == 1 and computer_choice == Rock:
    print("You won,user!")
elif User_input == 2 and computer_choice == Rock:
    print("You loose!")
elif User_input == 1 and computer_choice == Scissors:
    print("You loose!")
elif User_input == 0 and computer_choice == Paper:
    print("You loose!")'''

Games = [Rock,Paper,Scissors]
User_input = int(input("What do you want to choose? Type 0 for Rock,1 for paper and 2 for scissors\n"))
if User_input >= 3 or User_input < 0:
    print("It is an invalid number, try again!")
else:
    print("You chose:")
    print(Games[User_input])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(Games[computer_choice])

if User_input == 0 and computer_choice == 2:
    print("You win!")
elif User_input == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice > User_input:
    print("You lose!")
elif User_input > computer_choice:
    print("You win!")
elif User_input == computer_choice:
    print("Its a draw, try again!")


    
