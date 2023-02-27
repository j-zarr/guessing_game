"""A number-guessing game."""

"""A number-guessing game."""
import random

# Put your code here
name = input("Name:")
print(f'{name}, Im thinking of a number between 1 and 100')


def game():
    number = random.randint(1, 100)
    guess = int(input("Guess a number from 1 -100: "))
    while guess != number:
        if guess < number:
            print("too low")
            guess = int(input("Guess again number from 1 -100: "))
            print(guess)
        if guess > number:
            print("too high")
            guess = int(input("Guess again number from 1 -100: "))
            print(guess)
        
    print("Correct!")


game()


