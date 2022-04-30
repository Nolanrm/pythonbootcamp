#calculator

from art import logo
import os

x = 0
y = 0
result = 0
function = ""

print(logo)

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "div 0 error"
    return x/y


operations = {
    "+": add
    ,"-": subtract
    ,"*": multiply
    ,"/": divide
}



def calculator():

    x = float(input("what is the first number?: "))
    y = float(input("what is the second number?: "))
    should_continue = True
    for keys in operations:
        print(keys)
    function = input("pick an operation from the line above: ")

    result = operations[function](x,y)

    print(f"{x} {function} {y} = {result}")

    while should_continue:
        if input("would you like to continue with this calculation?(y/n)").lower() == 'y':
            x = result
            y = float(input("what number?: "))
            for keys in operations:
                print(keys)
            function = input("pick an operation from the line above: ")

            result = operations[function](x,y)
            print(f"{x} {function} {y} = {result}")
        else:
            if input("would you like to start over?").lower() == 'y':
                os.system('CLS')
                should_continue = False
                calculator()
            else:
                should_continue = False
                return print("finished")

calculator()
    


################
### multiple returns
################


# def is_leap(year):
#     """find if the year is a leap year"""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#              return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     leap_year_check = is_leap(year)
#     if leap_year_check:
#         month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     else:
#         month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return month_days[month]
        
    
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)