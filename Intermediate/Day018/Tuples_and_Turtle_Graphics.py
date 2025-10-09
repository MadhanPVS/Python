#************************           SECTION BEGINS           ************************#

# Tuples
'''
A tuple in Python is a built-in data type that allows you to create immutable sequences of values.
Elements can be access with index reference, similar to list.
'''
mytuple = ("apple", "banana", "cherry")
print(mytuple)

#------------------------------------------------------------------------------------#
# import
'''
Imports the entire module.
You need to use the module name as a prefix to access its functions, classes, or variables.
'''
import math

# from import
'''
Imports specific components (functions, classes, or variables) from a module.
You can directly use the imported component without the module name.
'''
from math import sqrt

# Alias modules
'''
In Python, you can use the as keyword to create an alias for an imported module. 
This is especially useful when the module name is long or when you want to make your code more concise and readable.
'''
import numpy as np
import pandas as pd

# installing modules
'''
Python modules can be installed using various methods, depending on your environment and requirements

1) pip install <module_name>
2) pip install <module_name>==<version>
3) pip install --upgrade <module_name>
'''
#------------------------------------------------------------------------------------#

# Turtle Graphics
'''
The turtle module in Python allows for unique and interactive graphics programming.
It provides a virtual canvas where you can control a turtle to draw shapes and patterns.
'''
def draw_square():
    from turtle import Turtle,Screen,colormode,bye
    import random
    turtle1 = Turtle()
    turtle1.shape("turtle")
    turtle1.color("red")
    for _ in range(4):
        turtle1.forward(100)
        turtle1.right(90)
    my_screen = Screen()
    my_screen.exitonclick()
        
def draw_dashed_line():
    from turtle import Turtle,Screen,colormode,bye
    import random
    turtle1 = Turtle()
    turtle1.shape("turtle")
    turtle1.color("red")
    for _ in range(10):
        turtle1.forward(10)
        turtle1.pendown()
        turtle1.forward(10)
        turtle1.penup()
    my_screen = Screen()
    my_screen.exitonclick()

def different_shapes():
    from turtle import Turtle,Screen,colormode,bye
    import random
    turtle1 = Turtle()
    turtle1.shape("turtle")
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]

    for i in range(3,11):
        turtle1.color(random.choice(colors))
        angle = 360/i
        for _ in range(i):
            turtle1.forward(100)
            turtle1.right(angle)
    my_screen = Screen()
    my_screen.exitonclick()

def random_walk():
    from turtle import Turtle,Screen,colormode,bye
    import random
    turtle1 = Turtle()
    turtle1.shape("turtle")
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black"]
    directions = [0, 90, 180, 270]
    for _ in range(200):
        turtle1.forward(30)
        turtle1.pensize(15)
        turtle1.speed("fastest")
        turtle1.color(random.choice(colors))
        turtle1.setheading(random.choice(directions))
    my_screen = Screen()
    my_screen.exitonclick()

def random_rgb():
    from turtle import Turtle,Screen,colormode,bye
    import random
    turtle1 = Turtle()
    colormode(255)
    turtle1.shape("turtle")
    turtle1.speed("fastest")
    directions = [0, 90, 180, 270]
    for _ in range(200):
        turtle1.forward(30)
        turtle1.pensize(15)
        turtle1.color(random_color())
        turtle1.setheading(random.choice(directions))
    my_screen = Screen()
    my_screen.exitonclick()
    
def spirograph():
    from turtle import Turtle,Screen,colormode,bye
    import random
    turtle1 = Turtle()
    colormode(255)
    turtle1.shape("turtle")
    turtle1.speed("fastest")  
    spirograph_gap(5,turtle1)
    my_screen = Screen()
    my_screen.exitonclick()

def spirograph_gap(size_of_gap,turtle_obj):
        for _ in range(int(360/size_of_gap)):
            turtle_obj.color(random_color())
            turtle_obj.circle(100)
            turtle_obj.setheading(turtle_obj.heading() + size_of_gap)

def random_color():
    import random
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) 
'''
call one of the below commented function at a time to see the output
'''
draw_square()
# draw_dashed_line()
# different_shapes()
# random_walk()
# random_rgb()
# spirograph()
#------------------------------------------------------------------------------------#

# Day018 Project
'''
Hirst Painting Project
refer URL - https://github.com/MadhanPVS/Python/tree/master/Intermediate/Day018/Project
'''

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Tuples_and_Turtle_Graphics.py
Version: v1.0
Created: 09/10/2025
Updated: 09/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
