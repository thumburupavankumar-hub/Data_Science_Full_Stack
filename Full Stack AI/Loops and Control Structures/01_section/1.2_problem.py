"""

Problem 1.2: Leap Year Checker (Medium)
Write a program to check if a given year is a leap year or not.

Rules:

A year is a leap year if it is divisible by 4
However, if it is divisible by 100, it is NOT a leap year
Exception: If it is also divisible by 400, then it IS a leap year
Examples:

2000: Leap year (divisible by 400)
1900: Not a leap year (divisible by 100 but not 400)
2024: Leap year (divisible by 4 but not 100)
Hint: Check conditions in order: first divisible by 400, then by 100, then by 4. Use modulo operator (%) to check divisibility.

"""

print("Leap year checker")

year = int(input("Enter year!"))

if year % 4 == 0:
    print("It's a leap year.")
elif year % 100 == 0:
    print("It's not a leap year.")
elif year % 400 == 0:
    print("It's a leap year.")
else:
    print("It's not a leap year.")