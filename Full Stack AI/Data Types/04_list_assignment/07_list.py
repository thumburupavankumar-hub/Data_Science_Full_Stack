# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]

list1 = [45, 67, 23, 89, 12, 34, 78]

sorted_list = sorted(list1, reverse= True)
second_largest = sorted_list[1]

max_num = max(list1)
list1.remove(max_num)
second_largest_alt = max(list1)

print(f"Second largest number : {second_largest}")