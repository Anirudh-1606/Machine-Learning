"""
Vegetable Selling ChatBot
1. Greeting the user
2. Menu
3. Respond to User's Input appropriately
4. Show the menu until the user prompts the Exit option
"""

import random
from menuopt import *

def greet():
    greetings = [
        "Love to Farm? Then you reached the right place! I am Kisan Bot",
        "Hi there! I am Kisan Bot, How can I help you?",
        "Hi, I am Kisan Bot, Always love to help you!"
    ]
    print()
    print(random.choice(greetings))
    print()

def menu():
    print("-----------WHAT DO YOU WANT ME TO DO?---------------")
    print("1. Vegetable Vendor")
    print("2. Farming Tips")
    print("3. Importance of Organic Farming")
    print("4. COVID-19 Awareness")
    print("5. QUIT")
    print("------------------------------------")
    print()
    try:
        return int(input("Enter your Choice [1-5]"))
        print()
    except:
        print("Only choose from 1,2,3 and 4")

def bot():
    greet()

    choice = menu()
    while choice!=5:
        if choice == 1:
            vendor()
        elif choice == 2:
            farming_tips()
        elif choice == 3:
            organic_farming()
        elif choice == 4:
            covid()
        else:
            print("I dont Know that")
        choice = menu()

bot()