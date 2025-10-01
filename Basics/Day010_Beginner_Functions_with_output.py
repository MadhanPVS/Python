#************************           SECTION BEGINS           ************************#

# Function with outputs
'''
The return statement in Python is used inside a function to send a value back to the caller. 
Once the return statement is executed, the function ends, and any code after it is ignored.
'''

def format_name(f_name, l_name):
    return (f"{f_name.title()} {l_name.title()}")

print(format_name("MaDhan","siVakumar"))

bool_leap_year = False
def is_leap_year(year):
    """
    Takes the year as argument to check if it is leap year
    """
    if year % 100 == 0:
        if year % 400 == 0:
            bool_leap_year = True
        else:
            bool_leap_year = False
    elif year % 4 == 0:
        bool_leap_year = True
    else:
        bool_leap_year = False
    return bool_leap_year
        
print(is_leap_year(2000))

'''
A function definition can be created inside another function
    def outer_function(a,b):
        def inner_function(c,d):
            return c + d
        return inner_function(a,b)
    print(outer_function(2,4))
'''
def outer_function(a,b):
    def inner_function(c,d):
        return c + d
    return inner_function(a,b)
print(outer_function(2,4))

'''
A function name can be assigned to another name
'''
def format_name(f_name, l_name):
    return (f"{f_name.title()} {l_name.title()}")
name_formatter = format_name #without parenthesis
print(name_formatter("madHan","sIvaKumar"))
#------------------------------------------------------------------------------------#

# Day010 Project
from os import system
#system("cls")
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide    
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an Operation: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation")
        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            system("cls")

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day010_Beginner_Functions_with_output.py
Version: v1.0
Created: 01/10/2025
Updated: 01/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
