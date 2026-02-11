"""

Problem 2.5: Prime Number Checker (Medium)
Write a program to check if a given number is prime or not.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Hint: Check if n is divisible by any number from 2 to n-1. If no divisor found, it's prime. Optimize: check only up to √n.

"""

print("Prime Number Checker\n")

number = int(input("Enter number : "))

if number <= 1:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")