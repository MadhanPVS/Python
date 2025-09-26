#************************           SECTION BEGINS           ************************#

# Module Imports
import random
#------------------------------------------------------------------------------------#

# For Loop
'''
Loops helps us to tell the computer to repeat or iterate over an action without have to write the code repeatedly.
for loop can be run along the list, range of numbers, tuples, string and dictionary, or on any iterable items.
'''
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)

student_scores = [98,97,89,80,90,100,98,78,85,83]

sum_val = 0
for score in student_scores:
    sum_val += score
print(f"Identified the sum value from the in-built function: {sum(student_scores)}")
print(f"Identified the sum value from the for loop: {sum_val}")

max_val = 0
for score in student_scores:
    if score > max_val:
        max_val = score
print(f"Identified max value from the in-built function: {max(student_scores)}")
print(f"Identified max value from the for loop: {max_val}")
#------------------------------------------------------------------------------------#

# Range function with For Loop
'''
Range function needs to be used along with one another function, mostly for loop function.
with the synrtax as: range(start, stop, step)
'''
total = 0
for number in range(1,101):
    total += number
print(total)

#FizzBuzz game [number divide by 3 - Fizz; number divide by 5 - Buzz; number divide by both 3 & 5 - FizzBuzz]
for number in range(1,101):
    if((number%3 == 0) and (number%5 == 0)):
        print("FizzBuzz")
    elif(number%3 == 0):
        print("Fizz")
    elif(number%5 ==0):
        print("Buzz")
    else:
        print(number)

#------------------------------------------------------------------------------------#

# Day005 Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']    

print("Welcome to the PyPassword Generator!")
numofLetters = int(input("How many letters would you like in your password?\n"))
numOfNumbers = int(input("How many numbers would you like in your password?\n"))
numOfSymbols = int(input("How many symbols would you like in your password?\n"))

#EasyPasswordVersion
password = ''
for char in range (0,numofLetters):
    password += random.choice(letters)
for char in range (0,numOfNumbers):
    password += random.choice(numbers)
for char in range (0,numOfSymbols):
    password += random.choice(symbols)
print(f"Easy Password: {password}")

#ComplexPasswordVersion
password_list = []
for char in range (0,numofLetters):
    password_list.append(random.choice(letters))
for char in range (0,numOfNumbers):
    password_list.append(random.choice(numbers))
for char in range (0,numOfSymbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ''
for char in password_list:
    password += char
print(f"Complex Password: {password})")

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day005_Beginner_Loops.py
Version: v1.0
Created: 26/09/2025
Updated: 26/09/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
