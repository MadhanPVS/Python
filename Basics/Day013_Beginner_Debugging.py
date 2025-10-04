#************************           SECTION BEGINS           ************************#

# Debugging
'''
1) Describe the problem
2) Gather information
3) Understand the function of code block
4) Fix the bug
'''
#___Bug
for i in range(1,20):
    if i == 20:
        print("you got it!")
#___Fix
for i in range(1,21): #Range increased to 21
    if i == 20:
        print("you got it!")

# Reproduce the Bug
#___Bug
from random import randint
dice_images = ["1","2","3","4","5","6"]
dice_num = randint(1,6)
print(dice_images[randint])
 #___Fix
from random import randint
dice_images = ["1","2","3","4","5","6"]
dice_num = randint(0,5) #Dice index changed as "0 to 5"
print(dice_images[randint])
#------------------------------------------------------------------------------------#

# try-except-finally
'''
try Block    : Contains the code that might raise an exception.
except Block : Handles specific exceptions that occur in the try block.
finally Block: Always executes, whether an exception occurs or not. 
               It's typically used for cleanup tasks like closing files or releasing resources.
'''
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

#------------------------------------------------------------------------------------#

# Day013 Project
'''
Debug the function to fix the logic/error
'''
def odd_or_even(number):
    if number % 2 != 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
'''
Debug the function to fix the logic/error
'''  
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return False
            else:
                return True
        else:
            return True
    else:
        return False
    
'''
Debug the function to fix the logic/error
'''
def fizz_buzz(target):
    for number in range(1, target):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day013_Beginner_Debugging.py
Version: v1.0
Created: 04/10/2025
Updated: 04/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''

