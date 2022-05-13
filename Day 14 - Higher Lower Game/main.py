import game_data as gd
import art as art
import random as rand
import os


def generate_options(game_data):
    number = rand.randint(0,len(game_data)) - 1
    return game_data[number]

options = []
correct_count = 0
continue_game = True


print(art.logo)

while continue_game == True:
    #add initial options
    while len(options) < 2:
        options.append(generate_options(gd.data))

    print(f'Higher or Lower? \n{options[0]["name"]} with {options[0]["follower_count"]} followers \n {art.vs} \n{options[1]["name"]}')

    user_choice = input(f'\"A\" if you think {options[1]["name"]} is higher or \"B\" if you think {options[1]["name"]} is lower: ').lower()

    if user_choice == 'a':
        if options[0]["follower_count"] < options[1]["follower_count"]:
            os.system('CLS')
            correct_count += 1
            print(f"Correct! You have {correct_count} correct answer(s)!")
        else:
            os.system('CLS')
            continue_game = False
            print(f'Wrong! \n{options[0]["name"]} has {options[0]["follower_count"]} followers \n{options[1]["name"]} has {options[1]["follower_count"]} followers ')
    if user_choice == 'b':
        if options[1]["follower_count"] < options[0]["follower_count"]:
            os.system('CLS')
            correct_count += 1
            print(f"Correct! You have {correct_count} correct answer(s)!")
        else:
            os.system('CLS')
            continue_game = False
            print(f'Wrong! \n{options[0]["name"]} has {options[0]["follower_count"]} followers \n{options[1]["name"]} has {options[1]["follower_count"]} followers ')

    while len(options) > 1:
        options.pop(0)




## pick two random entries
## keep 2nd option and make it first option and generate a new optoin
## giver user choice

## track if right or wrong
## track total score

