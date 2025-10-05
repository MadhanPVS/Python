#************************           SECTION BEGINS           ************************#

# Day014 Project

import Day014_Beginner_Higher_Lower_Game_ASCII_Art as art
import Day014_Beginner_Higher_Lower_Game_Data as dataSource
import random
from os import system
score = 0
current = {}
next = {}
answer = ""
choice = ""

def initialize(score,choice):
    #CURRENT DATA
    global current
    global next
    if score == 0:
        current = random.choice(dataSource.DATA)
    # elif choice == "A":
    #     current = current
    else:
        current = next
    name_current = current['name']
    description_current = current['description']
    follower_current = current['follower_count']
    country_current = current['country']
    
    #NEXT DATA
    next = random.choice(dataSource.DATA)
    while name_current == next['name']:
        next = random.choice(dataSource.DATA)
    name_next = next['name']
    description_next = next['description']
    follower_next= next['follower_count']
    country_next = next['country']
    
    print(f"Compare A: {name_current}, a {description_current}, from {country_current}")
    print(art.VERSUS)
    print(f"Against B: {name_next}, a {description_next}, from {country_next}")
    
    if follower_current > follower_next:
        return 'A'
    else:
        return 'B'

system("cls")
print(art.LOGO)
if score == 0:
    answer = initialize(score,choice)
choice = input("Who has more followers? Type 'A' or 'B': ")

while answer == choice:
    system("cls")
    score += 1
    print(art.LOGO)
    print(f"You're right! Current Score: {score}")
    answer = initialize(score,choice)
    choice = input("Who has more followers? Type 'A' or 'B': ")

print(f"Sorry, that's wrong. Final score: {score}")

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day014_Beginner_Higher_Lower_Game_Project.py
Version: v1.0
Created: 05/10/2025
Updated: 05/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''

