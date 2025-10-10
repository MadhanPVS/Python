#************************           SECTION BEGINS           ************************#

# Higher order functions
'''
A function qualifies as a HOF(Higher Order Function) if it either takes another function as an argument or returns a function as its result.
This allows for dynamic behavior and abstraction in code.
'''
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculate(n1, n2, func): # calculator is a higher order function
    return func(n1,n2)

print(calculate(2,3,add))

# Event Listener
'''
Event listeners are used to respond to specific events or triggers.
'''
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward) #no need to use parenthesis to pass the function as an argument in another function
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

#------------------------------------------------------------------------------------#

# Object state and instance
'''
Object:
The state of an object refers to the data or attributes that define its current condition.
These attributes are stored as instance variables within the object.
The state can change over time as the object's attributes are modified.
'''
class Car:
    def __init__(self, color, speed):
        self.color = color  # Attribute defining state
        self.speed = speed  # Attribute defining state

my_car = Car("Red", 120)

print(my_car.color)  # Output: Red
print(my_car.speed)  # Output: 120
my_car.speed = 150
print(my_car.speed)  # Output: 150

'''
Instance:
An instance is a specific object created from a class.
Each instance has its own state (attributes) and can behave independently of other instances.
Multiple instances of the same class can exist, each with unique attribute values.
'''
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance-specific attribute
        self.breed = breed  # Instance-specific attribute

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")
print(dog1.name, dog1.breed)  # Output: Buddy Golden Retriever
print(dog2.name, dog2.breed)  # Output: Max Beagle

#------------------------------------------------------------------------------------#

# Day019 Project
'''
Turtle Race
refer URL - https://github.com/MadhanPVS/Python/tree/master/Intermediate/Day019/Project
'''

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Instance_State_and_Higher_Order_Functions.py
Version: v1.0
Created: 10/10/2025
Updated: 10/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
