import random

#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#CODE
chosen_word = random.choice(word_list)
lenght_word = len(chosen_word)

display = []
global you_win
you_win = False
check = ""

# To create the display list of the same size of the word
for letter in chosen_word:
    display.append("_")

print(chosen_word)

while you_win == False:
    
    guess = input("Guess a letter: ").lower()

    for position in range(lenght_word):
        if chosen_word[position] == guess:
            display[position] = guess
    
    print(display)

    check = "".join(display)
        
    if check == chosen_word:
        print("You Win!!")
        you_win = True
    else: 
        continue

    

