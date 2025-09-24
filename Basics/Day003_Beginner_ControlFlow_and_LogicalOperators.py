#************************           SECTION BEGINS           ************************#

# If-Else and Conditional Statement
'''
The if-else statement in Python is a fundamental conditional structure used to execute a specific block of code based on whether the evaluated condition is True or False.
"if" should have a colon(:) at the end of the condition, and the required code block should begin after an indentation.
"else" should not have any condition, it is a default route incase of all the "if" statement are false. And, similar to "if", the code block of "else" also begins after an indentation.
'''
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
#------------------------------------------------------------------------------------#

# Nested-If statement
'''
A nested if statement in Python is an if statement placed inside another if or else block. This allows you to evaluate multiple conditions in a hierarchical manner.
'''
age = 20
citizenship = "Indian"

if age >= 18:
    print("You are eligible to vote.")
    if citizenship == "Indian":
        print("You can vote in India.")
    else:
        print("You cannot vote in India.")
else:
    print("You are not eligible to vote.")

#------------------------------------------------------------------------------------#

# Elif statement
'''
The elif keyword in Python is used for conditional statements, allowing you to check multiple conditions sequentially. 
It stands for "else if" and is used when the previous if or elif condition is not true, enabling you to test another condition.
'''
x = 15

if x < 10:
    print("x is less than 10")
elif x == 15:
    print("x is equal to 15")
else:
    print("x is greater than 10 but not 15")
    
#------------------------------------------------------------------------------------#

# Logical Operators
'''
Logical operators such as and, or, and not are often used in conjunction with if, elif, and else statements to evaluate multiple conditions.
'''
age = 25
income = 40000

if age < 18:
    print("You are a minor.")
elif age >= 18 and income < 30000:  # Logical AND operator
    print("You are an adult with low income.")
elif age >= 18 or income >= 30000:  # Logical OR operator
    print("You are an adult or have sufficient income.")
else:
    print("Condition not met.")
    
#------------------------------------------------------------------------------------#

# Day003 Project
print("Welcome to Python Parotta Deliveries!")
typeOfParotta = input("Which type of Parotta you want? M-Maida; W-Wheat; L-Layered Parotta").upper()
parottaQuantity = input("Total Quantity Required?")
omelette = input("Do you want 1-omelette with your Parotta? Y-Yes; N-No:").upper()
pepperChicken = input("Do you want 1-Pepper Chicken with your Parotta? Y-Yes; N-No:").upper()

bill = 0
if (typeOfParotta == "M"):
    bill += 10 * int(parottaQuantity)
elif (typeOfParotta == "W"):
    bill += 15 * int(parottaQuantity)
elif (typeOfParotta == "L"):
    bill += 30 * int(parottaQuantity)
else:
    print("Invalid Option")
if omelette == "Y":
    bill += 30
if pepperChicken == "Y":
    bill += 100
print(f"Your total bill is {bill}")

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day003_Beginner_ControlFlow_and_LogicalOperators.py
Version: v1.0
Created: 24/09/2025
Updated: 24/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
