"""

Problem 2.4: Fibonacci Series (Medium)
Write a program to print the first n terms of the Fibonacci series.

The Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Each number is the sum of the two preceding ones.

Hint: Initialize a=0, b=1. Print a, then in loop: calculate next=a+b, print next, then update a=b and b=next.

"""

print("Fibonacci Series\n")

number = int(input("Enter number : "))

a = 0
b = 1

if number <= 0:
    print("Please enter a positive number.")
else:
    print(a, end=" ")
    
    for num in range(1, number):
        next = a + b
        print(next, end=" ")
        a = b
        b = next