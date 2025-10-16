#************************           SECTION BEGINS           ************************#

from turtle import Turtle
import random

ALIGN = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,275)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGN,font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.",align=ALIGN,font=FONT)
        
            
#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
Project: Snake Game
File: scoreboard.py
Version: v1.0
Created: 12/10/2025
Updated: 12/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
