#************************           SECTION BEGINS           ************************#

# OOP - Basic Concepts
'''
Class: A blueprint for creating objects. It defines properties (attributes) and behaviors (methods).
Object: An instance of a class. It represents a specific entity created using the class blueprint.
Attributes: Variables defined in the class are termed as attributes.
Methods: function definition in the class is termed as Method.
'''

#------------------------------------------------------------------------------------#

# Turtle Class
'''
The turtle module in Python is a built-in library that provides a simple way to create graphics and drawings.
'''
from turtle import Turtle,Screen
turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("Red")
turtle1.forward(100)
my_screen = Screen()
my_screen.exitonclick()

#------------------------------------------------------------------------------------#

# PrettyTable Class
'''
The PrettyTable class in Python is used to create a visually appealing ASCII tables for displaying tabular data
'''
from prettytable import PrettyTable
table  = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)
table.align = "l"
print(table)
#------------------------------------------------------------------------------------#

# Day016 Project
'''
Coffee Machine project with OOP concept
refer URL - https://github.com/MadhanPVS/Python/tree/master/Intermediate/Day016/Project
'''

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: OOP.py
Version: v1.0
Created: 09/10/2025
Updated: 09/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
