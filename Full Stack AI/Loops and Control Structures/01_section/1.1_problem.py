# Section 1: Control Structures (If-Else Statements)

# Problem 1.1: Grade Calculator (Easy)

# Write a program that takes a student's marks (0-100) as input and prints their grade according to the following criteria:

# 90-100: Grade A
# 80-89: Grade B
# 70-79: Grade C
# 60-69: Grade D
# Below 60: Grade F
# Also, validate that the marks are within the valid range (0-100).

# Hint: Use if-elif-else statements. First check if marks are in valid range (0-100), then use >= comparisons starting from highest grade.

marks = int(input("Enter student marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")