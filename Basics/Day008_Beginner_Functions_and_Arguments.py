#************************           SECTION BEGINS           ************************#

# Function Parameters
'''
Functions can take the arguments by specifying the required number of parameters within the parenthesis.
Arguments can be of 2 types:
    1) Position Argument - are passed to a function in the same order as the parameters are defined. 
       The position of the argument are matters.
    2) Keyword Argument - are passed by explicitly specifying the parameter name. 
       The order does not matter as long as the parameter names are correct.
'''
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet("Alice",25) # Position Argument
greet(25,"Alice") # Position Argument - failure case
greet(age=25, name="Alice") # Keyword Argument
greet(name="Alice", age=25) # Keyword Argument

# Mini-Project
def calculate_love_score(name1,name2):
    name = name1 + name2
    love_score_lst = []
    true_love = [['T','R','U','E'],['L','O','V','E']]
    
    for list_item in true_love:
        total = 0
        for lst_letter in list_item:
            letter_count = 0
            for letter in name:
                if (letter.upper() == lst_letter.upper()):
                    letter_count += 1
            print(f"{lst_letter} occurs {letter_count} times")
            total += letter_count
        print(f"Total = {total}")
        love_score_lst.append(total)
    print(f"Love Score = {love_score_lst[0]}{love_score_lst[1]}")
calculate_love_score("love","love")
#------------------------------------------------------------------------------------#

# Day008 Project
should_continue = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount,encode_or_decode):
    output_text = ""    
    if encode_or_decode.lower() == "decode":
        shift_amount *= -1
        print(shift_amount)
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            print(output_text)
        else:            
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
            print(output_text)
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
while should_continue:
    cipherOption = input("Type 'encode' to encrypt; Type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text,shift_amount=shift,encode_or_decode=cipherOption)
    restart = input("Type 'Yes' if you want to go again. Otherwise, type 'no'.")
    if restart.lower() == "no":
        should_continue = False
        print("GoodBye!")
#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day008_Beginner_Functions_and_Arguments.py
Version: v1.0
Created: 29/09/2025
Updated: 29/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
