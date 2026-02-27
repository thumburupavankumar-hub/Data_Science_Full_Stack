"""

Problem 3.1: Reverse a Number (Medium)
Write a program that reverses the digits of a given number using a while loop.

Example: Input: 12345, Output: 54321

Hint: Initialize reverse=0. While n>0: get last digit (n%10), add to reverse (reverse=reverse*10+digit), remove last digit (n=n//10).

"""

print("Reversing a number")

number = int(input("Enter number to reverse : "))

reverse_num = 0

while number > 0:
    digit = number % 10
    reverse_num = reverse_num * 10 + digit
    number = number // 10
    
print(f"Reversed number is : {reverse_num}")