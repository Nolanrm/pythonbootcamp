#learn scope


#There is no block scope

import random

FINAL_ANSWER = random.randint(1,100)
CORRECT_ANSWER = False



def check_guess(guess,remaining_guesses):
    if guess > FINAL_ANSWER:
        remaining_guesses -= 1
        CORRECT_ANSWER = False
        print("Guess is too high")
        return  [remaining_guesses, CORRECT_ANSWER]
    elif guess < FINAL_ANSWER:
        remaining_guesses -= 1
        CORRECT_ANSWER = False
        print("Guess is too low")
        return [remaining_guesses, CORRECT_ANSWER]
    if guess == FINAL_ANSWER:
        print("Correct!")
        remaining_guesses = 0
        CORRECT_ANSWER = True
        return [remaining_guesses, CORRECT_ANSWER]


print("Welcome to the number guessing game \nI am thinking of a number between 1 and 100.")
difficulty = input("choose a difficulty, type 'hard' or 'easy': ").lower()

if difficulty == 'hard':
    remaining_guesses = 5
else:
    remaining_guesses = 10

while remaining_guesses > 0 and CORRECT_ANSWER == False:
    guess = int(input("Make a guess: "))

    response = check_guess(guess, remaining_guesses)
    remaining_guesses = response[0]
    CORRECT_ANSWER = response[1]
    if remaining_guesses > 0 and CORRECT_ANSWER == True:
        print(f'Winner correct number was {guess}')
    elif remaining_guesses == 0 and CORRECT_ANSWER == False:
        print(f'Out of guesses, correct answer was {FINAL_ANSWER}')
    else:
        print(f'you have {remaining_guesses} guesses remaining')


