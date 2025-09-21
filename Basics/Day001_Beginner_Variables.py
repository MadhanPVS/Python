#************************           SECTION BEGINS           ************************#

# Comments - To add notes
'''
Comments are used to add notes to your code, for future reference to yourself or to brief the functionality of your piece of code to other programmers.
Python supports single-line comment (#) and multi-line comments (a pair of 3 single quote). Comments are ignored while executing the program without any harm to the program functionality.
'''

#------------------------------------------------------------------------------------#

# Print the input text in the console
'''
print() is the keyword used to print the text in the console window, the string content within the parenthesis should be enclosed in the double quotes "".
The print function always has a newline character (\n) towards the end of characters. If you want to bring the subsequent lines in the same line, use the parameter (end='') in the print function.
'''

print("Hello World!")
print("This is line 1 \nThis is line 2 \nThis is line 3",end=' ')
print("I expect this to be printed in the same line at the end of previous print function")

#------------------------------------------------------------------------------------#

# Concatenation using print
'''
Multiple strings can be concatenated to form a sentence, just by adding the (+) sign. This is similar to the mathematical operation, but instead of performing arithmetic operations, it merges the string characters togethers.
'''
print("Hello,"+"This is how I concatenate the two strings without any space before the previous word") #Without space after words
print("Hello,"+" "+"This is how I concatenate the two strings by manually adding a space")
print("Hello,","This is how I concatenate the two strings with default space after a word by using a comma(,)")
#------------------------------------------------------------------------------------#

# Input Function - To get user inputs
'''
input() is the function used to get the user input, the executed command will wait for the user input to proceed further. This helps in reading the user input to perform certain set of operations over the input
'''

print("your name is : "+input("What is your name?"))
#------------------------------------------------------------------------------------#

# Variables - To store the values
'''
Variables in any programming language are used to store the data, which can then be used and manipulated throughout your code. 
The difference in Python is that you no need to declare the variable as int or string like the other languages, types will be explicitly inferred when the value is assigned to the variable.
The variable name should be meaningful, and relevant to the data value stored in the variable.
'''
userName = input("What is your name?") #userName is the variable to hold the value od user input
print("Hello " + userName + "!")
#------------------------------------------------------------------------------------#

# Day001 Project
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print("Your band name could be:", city_name, pet_name)

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day001_Beginner_Variables.py
Version: v1.0
Created: 15/08/2025
Updated: 21/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''

