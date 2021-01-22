#!/usr/bin/python3

import random

count=5
min=0
max=9
hidden = random.randrange(min, max)
print("I have picked one number between ", min, " and ", max, "please guess the number in", count, " tries")

steps = 0
while steps < count:
    guess = int(input("Enter your guess: "))
    steps = steps + 1
    if guess == hidden:
        print("Congratulations, hit in ", steps, "times")
        break
    elif guess < hidden:
        print("Your guess is too low, ", count - steps, "tries left")
    else:
        print("Your guess is too high, ", count - steps, "tries left")
