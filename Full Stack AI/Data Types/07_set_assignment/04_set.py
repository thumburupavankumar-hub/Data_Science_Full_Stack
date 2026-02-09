# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}

inter_set = my_set1 & my_set2

# we can also use
# inter_set = my_set1.intersection(my_set2)

print(f"Intersection set : {inter_set}")