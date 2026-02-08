# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577

num = [3.14, 2.718, 1.618, 0.577]
average = sum(num) / len(num)

print(f"Average: {average:.2f}")

# We can use for loop also

num = [3.14, 2.718, 1.618, 0.577]
l = len(num)
sum = 0

for i in num:
    sum += i
avg = sum / l

print(f"Average = {avg:.2f}")