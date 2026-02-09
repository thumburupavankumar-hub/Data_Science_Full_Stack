# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for num in numbers:
    if num % 2 == 0:
        sum += num
        
print(f"Sum of all even numbers {sum}")