#************************           SECTION BEGINS           ************************#

#Day019 Project
import os
import random
from turtle import Turtle,Screen

os.system("cls")
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "blue", "green", "purple", "orange", "pink", "brown"]
turtle_list = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    turtle_list.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
Project: Turtle Race
File: main.py
Version: v1.0
Created: 10/10/2025
Updated: 10/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
