import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def card_value():
    card_value = random.randint(1,12)
    return cards[card_value]

def hand_total(hand):
    total = 0
    for card in hand:
        total += card
    return total

 
player_hand = []
computer_hand = []
continue_playing = True

add_card = ''

while continue_playing:

    while len(player_hand) < 2:
        player_hand.append(card_value())
        computer_hand.append(card_value())

    print(f"your cards are {player_hand}")
    print(f"dealers first card {computer_hand[0]}")
    #check computers hand
    if hand_total(computer_hand) < 17:
        computer_hand.append(card_value())
    #check players hand
    if hand_total(player_hand) > 21:
        if 11 in player_hand:
            player_hand[player_hand.index(11)] = 1
        else:
            print(f'BUST with {player_hand}')
            continue_playing =  False
    else:
        add_card = input("hit? (y/n)").lower()

        if add_card == 'y':
            player_hand.append(card_value())
        else:
            continue_playing = False

if hand_total(player_hand) > 21:
    print('LOSER')
elif hand_total(player_hand) > hand_total(computer_hand):
    print(f'WINNER, \n your hand: {player_hand} \n computer hand: {computer_hand}')
elif hand_total(player_hand) == hand_total(computer_hand):
    print(f'DRAW \n your hand: {player_hand} \n computer hand: {computer_hand}')
elif hand_total(computer_hand) > 21:
    print(f'WINNER, computer BUST \n your hand: {player_hand} \n computer hand: {computer_hand}')
else:
    print(f"LOSER \n your hand: {player_hand} \n computer hand: {computer_hand}")

    
    

        

