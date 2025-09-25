# mini_projects/guess_the_number.py
# 🎲 Guess the Number Game
# A simple control flow mini project

import random

def guess_the_number():
    """Main function to run the guessing game."""
    secret_number = random.randint(1, 20)
    guess = None

    print("🎲 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 20.")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("✅ Correct! You guessed it.")

# run the game only if file is executed directly
if __name__ == "__main__":
    guess_the_number()

