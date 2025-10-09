#************************           SECTION BEGINS           ************************#

#Day018 Project
import colorgram
import os
import random
from turtle import Turtle,colormode,Screen

def read_color_pattern():
    rgb_colors = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "image.jpg")
    print(image_path)
    colors = colorgram.extract(image_path, 30)
    print(os.path)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r,g,b))
    print(rgb_colors)

color_list = []
read_color = input("Do you want to read the color pattern from image? (y/n)")
if read_color.lower == 'y':
    color_list = read_color_pattern()
else:
    color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle1 = Turtle()
turtle1.penup()
turtle1.hideturtle()
colormode(255)
turtle1.setheading(225)
turtle1.forward(300)
turtle1.setheading(0)
turtle1.speed("fastest")
number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    turtle1.dot(20,random.choice(color_list))
    turtle1.forward(50)    
    if (dot_count % 10 == 0):
        turtle1.setheading(90)
        turtle1.forward(50)
        turtle1.setheading(180)
        turtle1.forward(500)
        turtle1.setheading(0)

my_screen = Screen()
my_screen.exitonclick()

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
Project: Hirst Painting
File: main.py
Version: v1.0
Created: 09/10/2025
Updated: 09/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
