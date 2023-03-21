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

        ## ENCODE FUNCTION ##
        if direction == "encode":
            if shift > 25:
                tmp_new_index = 0
                count = shift
                while count > 0:
                    tmp_new_index +=1
                    count -=1
                    if tmp_new_index > 25:
                        tmp_new_index = 0
                new_index = index+tmp_new_index
                print(f'Esse é o new_index > 25 - {new_index}')
            else:
                new_index = index+shift
                print(f'Esse é o new_index < 25 - {new_index}')
            cipher_text = cipher_text + alphabet[new_index]
        
        ## DECODE FUNCTION ##
        elif direction == "decode":
            if shift > 25:
                tmp_new_index = 0
                count = shift
                while count > 0:
                    tmp_new_index +=1
                    count -=1
                    if tmp_new_index > 25:
                        tmp_new_index = 0
                shift = -abs(tmp_new_index)  
                new_index = index+shift
            else:
                shift = -abs(shift)
                new_index = index+shift
            cipher_text = cipher_text + alphabet[new_index]
    print(f"The {direction} text is {cipher_text}." )

#TODO-2: Call the caesaenr() function, passing over the 'text', 'shift' and 'direction' values.

ceasar(direction=direction, text=text, shift=shift)