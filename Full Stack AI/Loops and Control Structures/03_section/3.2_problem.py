"""

Problem 3.2: Sum of Digits (Easy)
Write a program that calculates the sum of all digits in a given number.

Example: Input: 12345, Output: 15 (1+2+3+4+5)

Hint: While n>0: add last digit to sum (sum += n%10), then remove it (n = n//10).

"""

print("Sum of Digits\n")

number = int(input("Enter number"))

sum = 0

while number > 0:
    sum += number % 10
    number = number // 10
    
print(f"Sum of digits : {sum}")