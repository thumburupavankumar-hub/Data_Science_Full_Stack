# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order

list1 = [64, 34, 25, 12, 22, 11, 90]

list1.sort(reverse=True)
        
print(f"Sorted list in decending order : {list1}")

# we can also use sorted function also

list1 = [64, 34, 25, 12, 22, 11, 90]

sorted_list = sorted(list1, reverse=True)
        
print(f"Sorted list in decending order : {sorted_list}")