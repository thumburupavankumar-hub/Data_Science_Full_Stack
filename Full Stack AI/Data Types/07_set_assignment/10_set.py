# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}

set1 = {1, 2, 3, 4, 5, 6}
subset1 = {1, 2, 3}

if subset1.issubset(set1):
    print(f"{subset1} is subset of {set1}")
else:
    print(f"{subset1} is not subset of {set1}")