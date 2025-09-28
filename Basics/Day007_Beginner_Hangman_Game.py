#************************           SECTION BEGINS           ************************#

# Day007 Hangman Game Project
import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#initialization
game_over = False
placeholder = "_"
display = ""
lives = 6
word_list = ["idly","dosa","biriyani","parota"]
chosen_word = random.choice(word_list)
display = placeholder * len(chosen_word)
correct_letters = []
print(display)


while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:        
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += placeholder
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")
    
    if "_" not in display:
        game_over = True
        print("You Win!")
    
    print(stages[6 - lives])


#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day007_Beginner_Hangman_Game.py
Version: v1.0
Created: 28/09/2025
Updated: 28/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
