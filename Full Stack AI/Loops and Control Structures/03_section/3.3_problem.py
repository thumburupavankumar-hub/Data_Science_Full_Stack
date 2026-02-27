"""

Problem 3.3: Number Guessing Game (Medium)
Write a number guessing game where:

The program generates a random number between 1 and 100
The user has to guess the number
After each guess, the program tells the user if their guess is too high or too low
The game continues until the user guesses correctly
Display the number of attempts taken
Hint: Use import random and random.randint(1, 100) to generate number. Use while loop with condition guess != target. Count attempts.

"""

import random

target = random.randint(1,100)

attempt_count = 0
guess = 0

while guess != target:
    guess = int(input("Enter your guess (1 - 100) : "))
    attempt_count += 1
    
    if guess < target:
        print("Too low! Try again.\n")
    elif guess > target:
        print("Too high! Try again.\n")
    else:
        print("\n🎉 Congratulations!")
        print("You guessed the number correctly!")
        print("Number of attempts:", attempt_count)