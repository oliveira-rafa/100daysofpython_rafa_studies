import random

#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 (Done) - Randomly choose a word from the word_list and assign it to a variable called chosen_word. 

#TODO-2 (Done) - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 (Done) - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#CODE
chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

# if guess in chosen_word:
#     print("Acertou Miseravi")
# else:
#     print("Não acertou")


print(chosen_word)
for letter in chosen_word:
    if letter == guess:
        print("Acertou miseravi!")
    else:
        print("Errou!")