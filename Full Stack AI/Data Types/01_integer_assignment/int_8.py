# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56

num = [15, 23, 31, 42, 56]
length = len(num)
sum = 0

for i in num:
    sum = sum+i
avg = sum / length

print(f"Average of {num} is {avg}")