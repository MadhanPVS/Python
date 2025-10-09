#************************           SECTION BEGINS           ************************#

# Day016 Project
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

system("cls")
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
Project: Coffee_Machine_with_OOP
File: main.py
Version: v1.0
Created: 09/10/2025
Updated: 09/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''


