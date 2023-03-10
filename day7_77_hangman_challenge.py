import random
import hangman_words
import hangman_art
import os

#Step 5

#DONE-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

#DONE-2: - Import the stages from hangman_art.py and make this error go away.

#DONE-3: - Import the logo from hangman_art.py and print it at the start 
# of the game.

#DONE-4: - If the user has entered a letter they've already guessed, print 
# the letter and let them know.

#DONE-5: - If the letter is not in the chosen_word, print out the letter and 
# let them know it's not in the word.

#TODO-6: EXTRA!! Desafio extra é fazer checar se o input é número ou tem mais
# de uma letra sendo enviada!


# VARIABLES 
stages = hangman_art.stages

logo = hangman_art.logo

word_list = hangman_words.word_list


global display
display = []
global end_game 
end_game = False
global lives 
lives = 6
global check 
check = ""
global guessed
guessed = []

#CODE
chosen_word = random.choice(word_list)
lenght_word = len(chosen_word)



# To create the display list of the same size of the word
for letter in chosen_word:
    display.append("_")

# Initial screen of the game
print(logo+"\n")

while end_game == False:
    
    guess = input("Guess a letter: ").lower()
    print("\n")

    os.system('clear')

    if guess in guessed:
      print(f"You tried {guess} before, please, try a diferent from the letters below.")
      print(f"{' ,'.join(guessed)}\n")
    else:
      guessed.append(guess)
      for position in range(lenght_word):
          if chosen_word[position] == guess:
              display[position] = guess 
              print(f"Great! The letter {guess} is in the word!\n")     
      if guess not in chosen_word:
        print(f"You guessed {guess}, but unfortunately this letter is not in the word.\n")
        lives -= 1
            
    print(f"Lives: {lives}/6")
    print(stages[lives])
    # print(display)
    print(f"{' '.join(display)}\n")

    check = "".join(display)
        
    if check == chosen_word:
        os.system("clear")
        print(logo+"\n")
        print("\n\nYOU WIN!!")
        end_game = True
    elif lives == 0:
        os.system("clear")
        print(logo+"\n")
        print("\n\nYOU LOST!!")
        end_game = True
    else: 
        continue

    