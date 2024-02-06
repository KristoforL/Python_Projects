#This project is making the coffee machine with OOPs concepts

import coffee_art as ca
import os
import sys as s

import money_machine as mm
import menu
import coffee_maker as cm


coffee_machine = cm.CoffeeMaker()
items = menu.Menu()
the_menu = menu.Menu()
the_money = mm.MoneyMachine()

def clear():
    """Clears the window based on the operating system"""
    if s.platform == "linux" or s.platform == "linux2":
        #linux
        os.system('clear')
    elif s.platform == "darwin":
        # OS X
        os.system("clear")
    elif s.platform == "win32":
        # Windows...
        os.system("cls")


on = True
while on:
    options = the_menu.get_items()
    order = input(f'What would you like? ({options}):\n').lower()

    if order =='off':
        print('Goodbye')
        on = False
    elif order == 'report':
        coffee_machine.report()
        the_money.report()
    else:
        drink = the_menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) and the_money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
        else:
            on = False

clear()
print('Thank you come again')








