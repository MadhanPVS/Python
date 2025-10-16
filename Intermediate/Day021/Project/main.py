#************************           SECTION BEGINS           ************************#

#Day021 Project - Continuation of Day20
import time
import os
from snake import  Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

os.system("cls")

snake = Snake()
food = Food()
screen = Screen()
scoreboard = Scoreboard()

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
    
    #Decect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Decect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.segments[1:]: #slicing the list to ignore the head piece
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
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
