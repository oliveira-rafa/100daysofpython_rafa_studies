from hashlib import new
from re import A
from art import *


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

tprint("Caesar \n Cipher", font="random")
# tprint("Cipher", font="bulbhead")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    cipher_text = ""

    for letter in text:
        index = alphabet.index(letter)

        if direction == "encode":
            new_index = index+shift
            cipher_text = cipher_text + alphabet[new_index]
        elif direction == "decode":
            shift = -abs(shift)  
            new_index = index+shift
            cipher_text = cipher_text + alphabet[new_index]
    print(f"The {direction} text is {cipher_text}." )



caesar(direction=direction, text=text, shift=shift)

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What happens if the user enters a number/symbol/space? Can you fix the code to keep the number/symbol/space when the text is encoded/decoded? e.g start_text = "Meet me at 3" -> end_text="**** ** ** 3"

#TODO-3: Can you figure out a way to ask the user if they want to restart the cipher program? e.g. Type 'yes' if you want to go again. Otherwise type 'no'. If they type 'yes' then as them for the direction/text/shift again and call the caesar() function again? Hint: Try creating a new function that calls itself if they type 'yes'.