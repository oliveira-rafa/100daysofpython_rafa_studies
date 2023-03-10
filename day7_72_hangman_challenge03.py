import random

#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#CODE
chosen_word = random.choice(word_list)
lenght_word = len(chosen_word)
guess = input("Guess a letter: ").lower()
display = []


# print(chosen_word)
# for letter in chosen_word:
#     display.append("-")

# print(display)


for position in range(len(chosen_word)):
    if chosen_word == guess:
        # print("Acertou miseravi!")
        display.append(guess)
    else:
        # print("Errou!")
        display.append("_")
    print(position)

print(display)