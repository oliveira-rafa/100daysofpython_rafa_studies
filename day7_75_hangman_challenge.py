import random

#Step 4

#DONE-1: - Create a variable called 'lives' to keep track of the number of 
# lives left. 
#Set 'lives' to equal 6.

 #DONE-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#DONE-3: - print the ASCII art from 'stages' that corresponds to the current 
# number of 'lives' the user has remaining.

# VARIABLES 
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

word_list = ["ardvark", "baboon", "camel"]


global display
display = []
global end_game 
end_game = False
global lives 
lives = 6
global check 
check = ""

#CODE
chosen_word = random.choice(word_list)
lenght_word = len(chosen_word)

# To create the display list of the same size of the word
for letter in chosen_word:
    display.append("_")

print(chosen_word)

while end_game == False:
    
    guess = input("Guess a letter: ").lower()

    for position in range(lenght_word):
        if chosen_word[position] == guess:
            display[position] = guess
    
    if guess not in chosen_word:
      lives -= 1
        

    print(stages[lives])
    print(display)
    print(lives)

    check = "".join(display)
        
    if check == chosen_word:
        print("You Win!!")
        end_game = True
    elif lives == 0:
        print("You Lost!!")
        end_game = True
    else: 
        continue

    