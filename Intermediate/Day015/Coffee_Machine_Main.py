#************************           SECTION BEGINS           ************************#

# Day015 Project
from os import system
MENU = {
"espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
"latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
"cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}
resources = {"water": 3000, "milk": 2000, "coffee": 1000}
profit = 0
machine_state = True

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def power_off():
    global machine_state
    system("cls")
    print("Machine has been turned off!")
    machine_state = False

def process_coins():
    print("Insert coins.")
    amount = int(input("Quarters: ")) * 0.25
    amount += int(input("Dimes: ")) * 0.10
    amount += int(input("Nickels: ")) * 0.05
    amount += int(input("Pennies: ")) * 0.01
    return amount

def check_resource(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")
    print(f"Report, after purcahsing {drink_name}")
    print_report()

while machine_state:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == 'report':
        print_report()
    elif user_input == 'off':
        power_off()
    else:
        try:
            drink = MENU[user_input]
        except KeyError:
            print("Invalid Selection, try again!")
            continue
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if payment >= drink["cost"]:
                print(f"Report, before purcahsing {user_input}")
                print_report()
                profit += drink["cost"]
                change = round(payment - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                make_coffee(user_input, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")

#************************           END OF SECTION           ************************#

'''
Author: Madhan PVS
File: Coffee_Machine_Main.py
Version: v1.0
Created: 06/10/2025
Updated: 06/10/2025

Reference:
1) Udemy - The Complete Python Pro BootCamp - Dr. Angela Yu
2) Coursera - Python for Everybody - Dr. Charles Severance
3) https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
'''

