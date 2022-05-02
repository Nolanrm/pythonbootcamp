import random

def card_value():
    card_value = random.randint(1,11)
    return card_value

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
    
    if hand_total(player_hand) > 21:
        print(f'BUST with {player_hand}')
        continue_playing =  False
    else:
        print(f"your cards are {player_hand}")
        print(f"dealers first card {computer_hand[0]}")

        add_card = input("hit? (y/n)").lower()

        if add_card == 'y':
            player_hand.append(card_value())
        else:
            continue_playing = False


