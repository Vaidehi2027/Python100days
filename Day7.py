#HANGMAN GAME
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
'''import random
random_index = random.randint(0,2)
chosen_word = word_list[random_index]
guess = input('Guess a letter: ')
guess_lower = guess.lower()
# for guess_lower in chosen_word:
for char in chosen_word:
  if guess_lower == char:
      print("Right")
  else:
      print("Wrong")'''

#TRAINERS WAY
'''import random
chosen_word = random.choice(word_list)
guess = input("Guess a letter").lower()
print(guess)
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")'''

#SECOND TRY
'''import random
word_list = ["aardvark", "baboon", "camel"] 
chosen_word = random.choice(word_list)
display=[]
for letter in chosen_word:
  display.append("_")
print(display)

end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")'''



# list1 = ['1','2','3']
# list1.reverse()
# print(list1)

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# stages.reverse()

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
          

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
      lives -= 1
      print(lives)
      if lives == 0:
        end_of_game = True
        print("You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

#FINAL CODE
#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# from hangman_words import word_list
# from hangman_art import logo
# from hangman_art import stages

print(logo)
print("Hey,lets see how good you are at words!")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print("You have already entered the letter" + guess)
      print(display)
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You are now remaining with {lives} lives!")
        print("You have guessed " + guess)
        print("Its not there in the word, try using another letter")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])

    
