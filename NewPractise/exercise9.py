# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:47:45 2021

@author: lenovo
"""

import random

number = random.randrange(1, 10)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("Please guess a number between 1 and 9. When you want to end the game print 'exit': ")

    if guess == "exit":
        print("Game Over")
        break

    guess = int(guess)
    count += 1
    if guess not in range(1, 10):
        print("You have to guess a number between 1 and 9!")
    elif guess < number:
        print("You've guessed too low!")
    elif guess > number:
        print("You've guessed too high!")
    else:
            print("You've got it! It took you {} tries!".format(count))
