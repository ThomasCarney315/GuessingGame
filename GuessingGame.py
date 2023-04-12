# Thomas Careny
# CIS 261 - Object-Oriented Computer Programming
# Guessing Game

import random

def display_heading():
    print('Guess The Number!')
    print('-' * 10)

def play():
    limit = int(input('Enter the limit:  '))
    num = random.randint(1, limit)
    print(f"\nOK, I'm thinking of a number from 1 to {limit}")
    guess = int(input('What is your guess?:  '))
    try_count = 1

    while guess != num:
        if guess > num:
            try_count += 1
            guess = int(input('Too high. Guess again:  '))
        elif guess < num:
            try_count += 1
            guess = int(input('Too low. Guess again:  '))
    print(f"You guessed the number in {try_count} trys")

def main():
    display_heading()
    play_or_not = 'y'
    while play_or_not == 'y':
        play()
        play_or_not = input('Play again? (y/n):  ').lower()
    print('Good Bye')

if __name__ == "__main__":
    main()