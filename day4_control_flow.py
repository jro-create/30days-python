# day4_control_flow.py
# Day 4: Control Flow (if/else + loops)

# --- IF STATEMENTS ---
# Control flow means: making decisions in your code.
# "If condition is True → do something, otherwise → do something else."

temperature = 35

if temperature > 30:
    print("It's hot outside!")
elif temperature >= 20:
    print("The weather is nice.")
else:
    print("It's a bit cold.")

age = 27 

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
else:
     print("Adult")

# --- FOR LOOP ---
# A for-loop repeats code a specific number of times, or goes through items in a collection.

print("\nCounting from 1 to 5 with a for loop:")
for i in range(1, 6):  # range(start, stop) goes up to stop-1
    print(i)

# Iterating through a string
word = "Python"
print("\nLetters in the word:")
for letter in word:
    print(letter)

# Print numbers 1-20, skipping multiples of 3, and stopping at 15

print("\nCounting from 1 to 20 with a for loop:")
for i in range (1, 21):
    if i == 15:        #stop if we reach 15
        print("Stopping at", i)
        break
    if i % 3 == 0:     # then skip multiples of 3
        continue
    print(i)

# --- WHILE LOOP ---
# A while-loop repeats as long as the condition is True.

count = 0
print("\nCounting with a while loop:")
while count < 5:
    print("Count is:", count)
    count += 1  # Same as count = count + 1

# --- BREAK & CONTINUE ---
# 'break' stops the loop completely.
# 'continue' skips the current iteration and jumps to the next.

print("\nDemonstrating break and continue:")
for i in range(1, 10):
    if i == 5:
        print("Breaking at", i)
        break
    if i % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", i)



# day4_control_flow.py#
print("\nGuess the Number Game with Random Secret:")

import random  # lets Python pick a random number

# pick a random secret between 1 and 20
secret_number = random.randint(1, 20)
guess = None

print("🎲 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 20.")

# loop until user guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! 🎉 You guessed it.")

