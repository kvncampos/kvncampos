# This is a guess the number game.

import random

print("Hello. What is your name?")
name = input().title()

print(F"Well, {name}, I am thinking of a number between 1-20.")
secretnumber = random.randint(1, 20)

for guesstaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess > secretnumber:
        print("Guess is too high.\n")
    elif guess < secretnumber:
        print("Guess is too low.\n")
    else:
        break # This condition is for the correct guess
if guess == secretnumber:
    print(f"Good job {name}, you guessed it!\n")
else:
    print(f"Nope, the number I was thinking of is {secretnumber}\n")

print(f"You took {guesstaken} tries to guess correctly.")
