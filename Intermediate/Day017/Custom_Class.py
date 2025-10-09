#************************           SECTION BEGINS           ************************#

# Custome_Class
'''
Classes in Python are a fundamental aspect of object-oriented programming (OOP). Creating a custom class in Python allows you to define your own data types and behaviors.
They provide a way to bundle data and functionality together, creating a new type of object that can have attributes and methods.
'''
# Empty Class
class Car:
    pass
car_1 = Car()

# User Class with follower features
class User:
    
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0 #no need to receive a parameter, it is a default value for new users
        self.following = 0 #no need to receive a parameter, it is a default value for new users
    
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("101","Madhan")
user_2 = User("102","Siva")
user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
#------------------------------------------------------------------------------------#

# Day017 Project
'''
Quiz Project
refer URL - https://github.com/MadhanPVS/Python/tree/master/Intermediate/Day017/Project
'''

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Custom_Class.py
Version: v1.0
Created: 09/10/2025
Updated: 09/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''
