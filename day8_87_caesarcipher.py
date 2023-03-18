from hashlib import new
from re import A


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def ceasar(direction, text, shift):
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

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

ceasar(direction=direction, text=text, shift=shift)