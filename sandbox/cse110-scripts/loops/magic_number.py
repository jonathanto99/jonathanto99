#magic_number
from random import*
import random
print()
magic_number = random.randint(1,100)

# print()
# magic_number = int(input("Enter the magic number: "))

guess = -100
user_guesses = 0  # Initialize a variable to store how many guesses the user has used
while guess != magic_number:
    guess = int(input("Enter a positive whole # guess: "))
    if guess > magic_number:
        print("Guess lower ")
    elif guess < magic_number: 
        print("Guess higher ")
    else:
        print("You guessed it! ")
    user_guesses += 1
    print()
print("You took {} guesses!".format(user_guesses))
print()

