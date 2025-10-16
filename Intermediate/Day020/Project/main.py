#************************           SECTION BEGINS           ************************#

#Day020 Project
import time
import os
import random
from turtle import Turtle,colormode,Screen
from snake import  Snake
os.system("cls")

snake = Snake()

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
Project: Snake Game
File: main.py
Version: v1.0
Created: 12/10/2025
Updated: 12/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
