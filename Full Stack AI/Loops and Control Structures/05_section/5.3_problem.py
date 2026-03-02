"""

Problem 5.3: Sum Until Negative (Medium)
Write a program that:

Keeps asking the user to enter numbers
Adds positive numbers to a sum
Skips zero (continues to next iteration)
Stops when a negative number is entered
Prints the final sum
Hint: Use while True loop. If num < 0, break. If num == 0, continue. Otherwise add to sum.

"""

total = 0

while True:
    user_input = input("Enter a number: ")

    # Check for empty input
    if user_input.strip() == "":
        print("Please enter a valid number.")
        continue

    try:
        num = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if num < 0:
        break
    elif num == 0:
        continue
    else:
        total += num

print("Final sum:", total)
