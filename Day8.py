#Jai mata di hum day 8 ko shuruvat karne wale hain
#FUNCTION REVISION
# def greet():
#   print ("Hello shashank")
#   print("Hello Arya, how are you?")
#   print("Namaste India!")
# greet()

#Functions with inputs
# def greet_with_name(name):
#     print(f"Hello,{name}!")
#     print(f"How do you do, {name} ?" )
# greet_with_name("Vaidehi")
# the name here is a parameter and the actual value of the name which is Vaidehi is called the argument
# The function with argumnets can be used to print different outputs and hence is handy

#Function with more than 1 input
# def greet(name,location):
#     print(f"Hello,{name}")
#     print(f"What is it like in {location}?")
# greet("Vaidehi","Pune")
# greet("Pune","Vaidehi")
# in positional arguments the poition matters trhe computeer doesnt understand what word means what so be cautious and use keyword arguments


# def vaidehi(name,location):
#     print(f"Hi,{name}")
#     print(f"Hello,{location}")
# vaidehi(location="Pune",name="Vaidehi")

#PAINT CALCULATOR
# import math
# def paint_calc(height,width,cover):
#     number_of_cans = math.ceil((height*width) / cover)
#     print(f"You will need {number_of_cans} number of cans")
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h,width=test_w,cover=coverage)
    
#PRIME NUMBER CHECKER
# def prime_checker(number):
#     if number ==1:
#         print("1 is neither prime nor composite")
#     elif number == 2:
#         print("Its the only even prime number!")
#     elif number % 2 != 0:
#         print("It is a prime number")
# n = int(input("Check this number: "))
# prime_checker(number=n)

# def prime_checker(number):
#     for num in range (2,number):
#         division = number%num
#     if division != 0:
#        print(f"{number} is a prime number.")
#     elif division == 0:
#        print(f"{number}it is not a prime number.")
# n = int(input("Check this number: "))
# prime_checker(number=n)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#   #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
# def encrypt(text_given,shift_position):
#   cypher_list = ""
#   for letter in text_given:
#     position = alphabet.index(letter)
#     new_position = position + shift_position
#     new_letter = alphabet[new_position]
#     cypher_list += new_letter
#   print(f"The encoded text is {cypher_list}")
# encrypt(text_given = text,shift_position = shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# from art import logo
# print(logo)
print("Lets play cipher!")
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"The {cipher_direction}d text is {end_text}")
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Type 'yes'if you want to go again.Otherwise type 'no'.\n")
  if result == 'no':
    should_continue = False
    print("Goodbye cipher!")







    


