# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
        
print(f"Afer removing duplicates : {unique_list}")