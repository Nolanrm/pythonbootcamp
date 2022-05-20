
import os


drink_machine = {
    'Water':50
    ,'Milk': 100
    ,'Money': 2.5
    ,'Ice Cream': 30
    ,'Sugar': 25
}

recipes = {
    'hot chocolate':{'Water': 10}
    ,'root beer float':{'Water': 10, 'Ice Cream':4}
    ,'frosty':{'Water': 10}
}
continue_service = True

def make_drink(drink):
    if drink == 'hot chocolate':
        if drink_machine['Water'] - recipes[drink]['Water'] > 0:
            drink_machine['Water'] -= recipes[drink]['Water']
        else:
            print('out of resources')
        return drink_machine
    elif drink == 'root beer float':
        pass
    elif drink == 'frosty':
        pass
    else:
        print("drink not found")

while continue_service ==True:
    #os.system('CLS')
    user_input = input('Place Order (type \"Hot Chocolate\"/\"Root Beer Float\"/\"Frosty\") \nSee Report (type \"report\") \nTurn machine off (type \"off\") \nWhat would you like: ').lower()

    if user_input == 'off':
        continue_service = False
    elif user_input == 'report':
        os.system('CLS')
        print(drink_machine)
    else:
        drink_machine = make_drink(user_input)
