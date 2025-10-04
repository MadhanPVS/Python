#************************           SECTION BEGINS           ************************#

# Scope of Variables
'''
Local Variables are declared inside a function and are accessible only within that function.
Global Variables are declared outside any function and are accessible throughout the program.
'''

apple = 1 # global variable
def increase_apple():
    apple = 2 # local variable
    print(f"Apples inside function {apple}")

increase_apple()
print(f"Apples outside function {apple}")

# Modifying global variable from local code block
apple = 1 # global variable
def increase_apple():
    global apple # use global variable
    apple += 1 
    print(f"Apples inside function {apple}")

increase_apple()
print(f"Apples outside function {apple}")
#------------------------------------------------------------------------------------#

# Check Prime Number or Not
'''
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Examples include 2, 3, 5, 7, and 11

Optimized method:
if a number has a factor larger than its square root, the corresponding smaller factor would have already been found. 
So we only need to check up to √num
Example: To check 16 is a prime number, we no need to check all the number range from 2 to 16.
It is enough to check upto √16=4 [2,3,4]
'''
def is_prime(num):
    if num <= 1:
        return False
    print(num, num**0.5,int(num**0.5) + 1)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(30))

#------------------------------------------------------------------------------------#

# Day012 Project

import random
from os import system

LOGO = """
  ____                       _   _                                  _               
 / ___|_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  
"""

EASY_ATTEMPTS = 10 # global constant
HARD_ATTEMPTS = 5 # global constant


def check_answer(user_guess, actual_number):
    """
    Checks answer against guess, returns the number of turns remaining
    """
    if user_guess > actual_number:
        print("Too high.")
        return False
    elif user_guess < actual_number:
        print("Too low.")
        return False
    else:
        print(f"Congtrats! you got the number, it is {actual_number}")
        return True


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def game():
    system("cls")
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100..")
    num_to_find = random.randint(1,100)
    is_game_over = False
    is_answer_found = False
    guessed_number = 0
    attempts = set_difficulty()

    while not is_game_over:
        
        print(f"You have {attempts} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess: "))
        is_answer_found = check_answer(guessed_number, num_to_find)
        if is_answer_found == True:
            return 0
        attempts -= 1
        if attempts == 0:
            print(f"You have 0 attempt remaining, you lose!")
            return 0
game()

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day012_Beginner_Scope_Of_Variables.py
Version: v1.0
Created: 04/10/2025
Updated: 04/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''

