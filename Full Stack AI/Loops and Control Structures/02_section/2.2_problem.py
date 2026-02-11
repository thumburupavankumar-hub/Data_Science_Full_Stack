"""

Problem 2.2: Factorial Calculator (Medium)
Write a program to calculate the factorial of a number using a for loop.

Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1

Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

Hint: Initialize result = 1. Use for loop with range(1, n+1) and multiply result by each number.

"""

print("Factorial Calculator\n")

number = int(input("Enter number : "))

factorial = 1

for num in range(1, number + 1):
    factorial *= num
    
print(f"Factorial of {number} : {factorial}")