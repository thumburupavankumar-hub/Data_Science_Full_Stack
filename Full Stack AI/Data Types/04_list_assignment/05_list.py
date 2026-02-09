# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]

num_list = [15, 23, 31, 42, 56, 78, 91]

total = 0

for num in num_list:
    total += num
    
average = total / len(num_list)
    
print(f"Total sum : {total}")
print(f"Average : {average}")