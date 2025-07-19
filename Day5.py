# Hello! WELCOME TO DAY5 , TODAY WE GONNA BE BUILDING A PASSWORD GENERATOR!
#LOOPS
'''Fruits = ["Apple","Banana","Pear"]
for fruit in Fruits:
    print(fruit)
    print(fruit + " pie")
    print(Fruits)
print(Fruits) # remember this line is out of the for loop and hence it will print the lsit of Fruits just once'''

'''students_height = input("Gimme a list of heights of studens in cms:\n").split(' ')
n = 0
for n in range(0,len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)
print(type(students_height[1]))

# REPLICATION OF THE SUM FUNCTION
total_height = 0
for height in students_height:
    total_height += height
print(total_height)

#REPLICATING THE LENGTH FUNCTION
total_length = 0
for number in students_height:
    total_length += 1
print(total_length)

average_height = round(total_height / total_length)
print(f"The average height required is {average_height}")'''

#FINDING THE MAXIMUM SCORE FROM THE LIST OF SCORES
'''student_scores = input("Gimme the list of students scores").split(' ')
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
for i in range(0,len(student_scores)-1):
    if student_scores[i] > student_scores[i+1]:
        print(student_scores[i])'''

# TRAINER'S CODE
'''student_scores = input("Gimme the list of students scores").split(' ')
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
maximum_score = 0
for score in student_scores:
    if score > maximum_score:
        maximum_score = score
print(f"The maximum score is {maximum_score}")'''

#RANGE FUNCTION
#PRINTING SUM OF FIRST 100 NUMBERS
'''total = 0
for number in range(1,101):
    total += number
print(total)'''

#PRINTING THE SUM OF ALL EVEN NUMBERS FROM 1 TO 100
'''total_even = 0
for number in range (2,101,2):
    total_even += number
print(total_even)'''

#ANOTHER WAY TO PRINT THE SUM OF EVEN NUMBERS
'''total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)'''

#THE FIZZBUZZ GAME
'''for number in range(1,100):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
        if  number % 15 == 0:
          print ("FizzBuzz")
    else:
        print (number)'''

#PASSWORD GENERATOR
import random
letters = ['a','b','c','d','e','f','g','h,','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G'
'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to PYPassword Generator!")
nr_letters = int(input("How many letters would you like in the password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like i your password? "))
# password = ''
'''for char in range(0,nr_letters):
    random_char = random.choice(letters)
    password += random_char
for sym in range(0,nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
for num in range(0,nr_numbers):
    random_number = random.choice(numbers)
    password += random_number
print("This is your required password is: " + password)'''
password = []
for char in range(0,nr_letters):
    random_char = random.choice(letters)
    password += random_char
for sym in range(0,nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
for num in range(0,nr_numbers):
    random_number = random.choice(numbers)
    password += random_number

random.shuffle(password)
password_final = ''
for char in password:
    password_final += char
print("Your final password is" + password_final)
    








