#************************           SECTION BEGINS           ************************#

# Data Types
'''
int - An integer is a whole number, positive or negative, without any decimal point. Python integers can be arbitrarily large, limited only by the available system memory.
float - A float in python is a real number with decimal point. Python floats have limited precision and may sometimes can cause rounding off error
string - A string is a sequence of characters enclosed in a single quote or double quote, it supports unicode characters. Strings are immutable, we can access the character of a string using index but cannot be replaced with other character like the list.
bool - Boolean values are used in decision or toggling function
'''
a = 5 #int
print(type(a))

b = 5.0 #float
print(type(b))

c = "sample_text" #string
print(type(c))

d = True # boolean
print(type(d))
#------------------------------------------------------------------------------------#

# Basic Type Conversion
'''
Similar to wide other languages, Python has 2 different type conversions:-
1) Implicit Type Conversion - The Python interpreter has the ability to automatically converts from one data type to another without any user interactions.
2) Explicit Type Conversion - Forced by user to convert from one data type to other, there is a risk of data type violation or data loss, it is best practices to include Try/Except blocks
'''

# 1) Implicit Type Conversion
x = 5
print("Type of x:",type(x)) #Output: Type of x: <class 'int'>

y = 15.6
print("Type of y:",type(y)) #Output: Type of x: <class 'float'>

z = x + y
print(z) 
print("Type of z:",type(z)) #Output: Type of x: <class 'float'>
#____________________________________________________________________________________#

# 2) Explicit Type Conversion
# ____initializing string____
input_string = "1001"
print("Initialized String: ",input_string) #1001

# string to integer Base 2
result_int = int(input_string,2)
print ("Post conversion of string to Int: ", end="")
print (result_int) #9
 
# string to float
result_float = float(input_string)
print ("Post conversion of string to float : ", end="")
print (result_float) #1001.0

# ____initializing integers____
num1 = 24
num2 = 77
print("Initialized Integer1: ",num1) #24
print("Initialized Integer2: ",num2) #77

# integer to complex number
result_complex = complex(num1,num2)
print ("Post conversion of integer to complex number : ",end="")
print (result_complex) #(24+77j)
 
# integer to string
result_string = str(num1)
print ("Post conversion of integer to string : ",end="")
print (result_string) #24

# integer to ASCII
result_ASCII = chr(num2)
print ("Post conversion of integer to ASCII : ",end="")
print (result_ASCII) #M

# ____initializing string____
input_string = 'Python'
print("Initialized String: ",input_string) #Python
 
# string to tuple
result_tuple = tuple(input_string)
print ("Post conversion of string to tuple : ",end="")
print (result_tuple)
 
# string to set
result_set = set(input_string)
print ("Post conversion of string to set : ",end="")
print (result_set)

# string to list
result_list = list(input_string)
print ("Post conversion of string to list : ",end="")
print (result_list)

# ____initializing list____
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
list_of_lists = [['a', 1], ['b', 2], ['c', 3]]

print("Initialized list_of_tuples: ",list_of_tuples) #Python
print("Initialized list_of_lists: ",list_of_lists) #Python

# list_of_tuples to dictionary
result_dictionary = dict(list_of_tuples)
print("Post conversion of list_of_tuples to dictionary",result_dictionary) #Output: {'a': 1, 'b': 2, 'c': 3}

# list_of_lists to dictionary
result_dictionary = dict(list_of_lists)
print("Post conversion of list_of_lists to dictionary",result_dictionary) #Output: {'a': 1, 'b': 2, 'c': 3}

# ____initializing tuple____
input_tuple = (('a', 1) ,('f', 2), ('g', 3))
print("Initialized tuple: ",input_tuple) #Python

# tuple to dictionary
result_dictionary = dict(input_tuple)
print ("Post conversion of tuple to dictionary : ",end="")
print (result_dictionary)
#------------------------------------------------------------------------------------#

# Operators
'''
Following are the 4 major Python operators:
1) Arithmetic operators - Arithmetic operators are used with numeric values to perform common mathematical operations [(), **, {* or / or // or %}, {+ or -}]
2) Assignment operators - Assignment operators are used to assign values to variables [=, +=, -=, *=, /=]
3) Comparison operators - Comparison operators are used to compare two values of a variable and returns boolean result [==, != , >, <, >=, <=]
4) Logical operators - Logical operators are used to combine the 2 or more conditional statements [(), not, and, or]

Also, there are other Operators like Identity Operator and Bitwise Operator {will be covered in future version}
'''
# Arithmetic Operator
a = 7
b = 2
print ('Sum: ', a + b) # Addition
print ('Subtraction: ', a - b) # Subtraction
print ('Multiplication: ', a * b) # Multiplication
print ('Division: ', a / b) # Division
print ('Floor Division: ', a // b) # Floor Division
print ('Modulo: ', a % b) # Modulo
print ('Power: ', a ** b) # Exponent

# Assignment operator
a = 10 # assign 10 to a
b = 5 # assign 5 to b
a += b # # do sum of a and b, then assing back to a like [a = a + b]
print(a) #15

# Comparison operator
a = 5
b = 2
print (a > b) # True

# Logical operator
a = 5
b = 6
print((a > 2) and (b >= 6)) # True
#------------------------------------------------------------------------------------#

# F String
'''
F-string are simple and an efficient way to embed the variables with the string. 
In regular string we need to concatenate the variables with the explicit type conversion if required. 
F-String makes is simpler with a pair of curly braces. Values are auto formatted to string to fit among the literals.

'''
#Without F-string
name = str(input("What is your name? "))
age = int(input("What is your age? "))
print("Hello, My name is " + name + " and I'm " + str(age) + " years old.") # explicit conversion of integer to string

#With F-string
name = str(input("What is your name? "))
age = int(input("What is your age? "))
print(f"Hello, My name is {name} and I'm {age} years old.")
#------------------------------------------------------------------------------------#

# Day002 Project
print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_per_person = total_bill / people
gross_bill = round(bill_per_person,2)

print(f"Each person should pay: ${gross_bill}")

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day002_Beginner_DataTypes.py
Version: v1.0
Created: 23/09/2025
Updated: 23/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
