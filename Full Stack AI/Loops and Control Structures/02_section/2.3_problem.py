"""

Problem 2.3: Sum of Even Numbers (Easy)
Write a program that calculates the sum of all even numbers between 1 and n (inclusive), where n is provided by the user.

Example: If n = 10, sum = 2 + 4 + 6 + 8 + 10 = 30

Hint: Use for loop with range(1, n+1). Check if i % 2 == 0, then add to sum. Or use range(2, n+1, 2) to iterate only even numbers.

"""

print("Sum of Even Numbers\n")

number = int(input("Enter number : "))

sum = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        sum += num
        
print(f"Sum of Even Numbers : {sum}")