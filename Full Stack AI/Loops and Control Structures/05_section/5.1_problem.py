"""

Problem 5.1: Find First Multiple (Easy)
Write a program that finds and prints the first number in the range 1 to 100 that is divisible by both 7 and 13.
Use the break statement to exit the loop once found.

Hint: Loop through 1 to 100. Check if i%7==0 and i%13==0. If true, print i and use break to exit loop.

"""
    
for i in range(1, 101):
    if i % 7 == 0 and i % 13 == 0:
        print(f"First number in the range 1 to 100 that is divisible by both 7 and 13 : {i}")
        break