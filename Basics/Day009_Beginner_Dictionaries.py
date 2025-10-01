#************************           SECTION BEGINS           ************************#

# Dictionary
'''
A dictionary in Python is a data structure that allows us to associate a key to a value and pairs together.
{"key1" : "value1",
 "key2" : "value2"}
'''

colours = {    
    "apple":"red",
    "pear":"green",
    "banana":"yellow"
}
print(colours["apple"])

#adding new key
colours["mango"] = "yellow"
print(colours)

#modify existing value
colours["apple"] = "green"
print(colours)

# loop through data
for key in colours:
    print(f"color of {key} is {colours[key]}")

#wipeout data
colours = {}
print(colours)

# Mini Project
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades ={}

for key in student_scores:
    mark = student_scores[key]
    if 91 <= mark <= 100:
        grade = "Outstanding"
    elif 81 <= mark <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= mark <= 80:
        grade = "Acceptable"
    elif mark <= 70:
        grade = "Fail"
    student_grades[key] = grade
print(student_scores)
print(student_grades)
#------------------------------------------------------------------------------------#

# Nesting Dictionary
'''
Nesting a list or dictionary to a dictionary to form a complex data structure
'''
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
travel_log = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany" : ["Berlin","Stuttgart",["Munich","Hamburg"]]
}
print(travel_log["France"][1])
print(travel_log["Germany"][2][1])

India_travel_log = {
    "Tamilnadu" : {"Villupuram":10,"Chennai":5,"Trichy":2},
    "Germany" : ["Berlin","Stuttgart",["Munich","Hamburg"]]
}
print(India_travel_log["Tamilnadu"]["Villupuram"])
#------------------------------------------------------------------------------------#

# Day009 Project
from os import system

print("Welcome to the secret auction program.")
to_Continue = True
bid_summary = {}
max_bid = 0

while to_Continue:
    name = input("What's your name?")
    amount = input("What's your bid?")
    anyoneElse = input("Are there any other bidders? Type 'yes' or 'no'.")
    bid_summary[name] = amount    
    if anyoneElse.lower() == "no":
        to_Continue = False
    system("cls")

for key in bid_summary:
    if int(bid_summary[key]) > int(max_bid):
        max_bid = bid_summary[key]

bidders = [k for k,v in bid_summary.items() if int(v) == int(max_bid)]

print(f"The highest bidders are {bidders} with the bid amount {max_bid}")

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Day009_Beginner_Dictionaries.py
Version: v1.0
Created: 01/10/2025
Updated: 01/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
