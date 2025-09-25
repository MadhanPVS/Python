#************************           SECTION BEGINS           ************************#

# Module Imports
import random
#------------------------------------------------------------------------------------#

# Lists
'''
List are python data structure used to store multiple items of different data types.
List are mutable, the list items can inserted, modified or deleted at any required position.
'''

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0]) #apple
print(fruits[2]) #cherry
print(fruits[-1]) #cherry
print(fruits[-2]) #banana

fruits.append("orange") #Using append() to add an element at the end
print(fruits)
fruits.insert(1, "blueberry") #Using insert() to add an element at a specific position
print(fruits)
fruits.extend(["grape", "pineapple"]) #Using extend() to add multiple elements at the end
print(fruits)

fruits.remove("banana") #Using remove() to remove a specific element
print(fruits)
fruits.pop(2) #Using pop() to remove an element at a specific position
print(fruits)
del fruits[1] #Using del to remove an element at a specific position
print(fruits)
    
#------------------------------------------------------------------------------------#

# Randomisation
'''
The random module in Python is a built-in library used to generate pseudo-random numbers and perform random operations.
It provides a variety of functions to work with random numbers, sequences, and distributions.


1) Generate Random Numbers:
random.random(): Returns a random float between 0.0 and 1.0.
random.randint(a, b): Returns a random integer between a and b (inclusive).
random.uniform(a, b): Returns a random float between a and b .

2) Work with Sequences:
random.choice(seq): Returns a random element from a sequence (e.g., list, tuple).
random.shuffle(seq): Shuffles the elements of a sequence in place.
random.sample(seq, k): Returns a list of k unique random elements from a sequence.

3) Distributions:
random.gauss(mu, sigma): Generates a random number following a Gaussian distribution with mean mu and standard deviation sigma.
random.expovariate(lambd): Generates a random number following an exponential distribution.

4) Seed for Reproducibility:
random.seed(x): Initializes the random number generator with a seed value x. This ensures reproducibility of random sequences.
'''
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors)) #random element from list
print(random.randint(1, 10)) #random int value between 1 and 10
print(random.random()) #random float value [0.0 <= N < 1.0]

#------------------------------------------------------------------------------------#

# Day004 Project

# Rock, Paper, Scissors Game with Random Module

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [Rock, Paper, Scissors]

user_choice = int(input("What do you choose? Type 0=Rock; 1=Paper; 2=Scissors\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
    
computer_choice = random.randint(0,2)
print("Computer Chose:")
print(game_images[computer_choice])

# Game Rules
if user_choice >=3 or user_choice < 0:
    print("Invalid Selection, You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice > user_choice:
    print("You Lose!")
elif computer_choice == user_choice:
    print("It's a Draw!")
    
#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day004_Beginner_Randomisation_and_Lists.py
Version: v1.0
Created: 25/09/2025
Updated: 25/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
