# import turtle

# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('#6495ED')
# timmy.forward(20)
# timmy.right(90)
# timmy.forward(100)

# my_screen = turtle.Screen()
# my_screen.exitonclick()


# import prettytable

# table = prettytable.PrettyTable()

# table.add_column('pokemon name',['pikachu','squirtle','charmander'])
# table.add_column('type',['electric','water','fire'])
# table.align = 'l'
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

machine_on = True
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()

while machine_on == True:
    
    customer_request = input(f'what would you like to order {my_menu.get_items()}?').lower()

    if customer_request == 'off':
        os.system('CLS')
        machine_on = False
    elif customer_request == 'report':
        os.system('CLS')
        print(coffee_machine.report())
    else:
        os.system('CLS')
        drink = my_menu.find_drink(customer_request)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
            else:
                pass



