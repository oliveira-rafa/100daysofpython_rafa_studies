from hashlib import new
from re import A
from art import *


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

tprint("Caesar \n Cipher", font="colossal")
# tprint("Cipher", font="bulbhead")

def caesar(direction, text, shift):
    cipher_text = ""

    for letter in text:
        if letter in alphabet:
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
                    # print(f'Esse é o new_index > 25 - {new_index}')
                else:
                    new_index = index+shift
                    # print(f'Esse é o new_index < 25 - {new_index}')
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
        elif letter not in alphabet:
            cipher_text = cipher_text+letter

    print(f"The {direction} text is '{cipher_text}'." )
    


end_program = False
while end_program == False:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(direction=direction, text=text, shift=shift)

    resp_end_program = input(f'Do you want to try again? Y or N: ').lower()
    if resp_end_program == 'y':
        end_program = False
    else:
        end_program = True



#DONE#TODO-1: Import and print the logo from art.py when the program starts.

#DONE#TODO-2: What happens if the user enters a number/symbol/space? Can you fix the code to keep the number/symbol/space when the text is encoded/decoded? e.g start_text = "Meet me at 3" -> end_text="**** ** ** 3"

#DONE#TODO-3: Can you figure out a way to ask the user if they want to restart the cipher program? e.g. Type 'yes' if you want to go again. Otherwise type 'no'. If they type 'yes' then as them for the direction/text/shift again and call the caesar() function again? Hint: Try creating a new function that calls itself if they type 'yes'.