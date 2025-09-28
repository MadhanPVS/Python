#************************           SECTION BEGINS           ************************#

# Module Imports
import random
#------------------------------------------------------------------------------------#

# Indentation in Python
'''
Python indentation is to group the statements into blocks, such as loops, conditionals, and functions.
All statements within the same block must have the same level of indentation
The Python community recommends using 4 spaces per indentation level for consistency.
You can use spaces or tabs, but mixing them is not allowed.
'''

# While Loop
'''
While loop in Python is used to repeatedly execute a block of code as long as a specified condition evaluates to True.
It is particularly useful when the number of iterations is not known beforehand.
Use for loops when you know how many times the loop should run.
Use while loops when the loop depends on a condition that may change dynamically.
'''
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

#------------------------------------------------------------------------------------#

# Functions
'''
A function is a block of reusable code that performs a specific task.
Functions help in organizing code, making it modular, and reducing redundancy.
'''
def greet(name):
    """This function greets the person passed as an argument."""
    print(f"Hello, {name}!")

greet("Madhan")

#------------------------------------------------------------------------------------#

# Day006 Project
def calculate_sum():
    total = 0
    while True:
        number = int(input("Enter an integer number (or a 0 to stop): "))
        if number == 0:
            break  # Exit the loop if the number is 0
        total += number  # Add the number to the total
    return total

# Call the function and display the result
result = calculate_sum()
print(f"The total sum of the entered numbers is: {result}")


#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day006_Beginner_Loops_and_Functions.py
Version: v1.0
Created: 27/09/2025
Updated: 28/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
