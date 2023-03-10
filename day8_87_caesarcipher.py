from hashlib import new
from re import A


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def encrypt(text,shift):
    cipher_text = ""

    for letter in text:
        index = alphabet.index(letter)  
        
        new_index = index+shift

        cipher_text = cipher_text + alphabet[new_index]
    
    print(f"The encoded text is {cipher_text}.")


def decrypt(text,shift):

    cipher_text = ""

    for letter in text:
        index = alphabet.index(letter)

        shift = -abs(shift)  
        
        new_index = index+shift

        cipher_text = cipher_text + alphabet[new_index]
    
    print(f"The encoded text is {cipher_text}.")

if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("Please try encrypt or decrypt")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.