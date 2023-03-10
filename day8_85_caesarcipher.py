from hashlib import new
from re import A


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

def encrypt(text,shift):
    cipher_text = ""
    new_index = 0

    for letter in text:
        index = alphabet.index(letter)  
        
        new_index = index+shift

        cipher_text = cipher_text + alphabet[new_index]
    
    print(f"The encoded text is {cipher_text}.")

encrypt(text,shift)


# Comentario:
"""
A professora usou o esquema de dobrar o tamanho da lista pra não mexer na lógica
mas na real isso vai continuar dando problema se o shift for maior do que o
tamanho da lista. Só resolve se você continuar usando um tamanho de shift menor
do que o tamanho da lista.

Acho interessante desenvolver um método que funcione com qualquer shift.

Gastei muito tempo sem muito sucesso e larguei pra la. kkkk
"""