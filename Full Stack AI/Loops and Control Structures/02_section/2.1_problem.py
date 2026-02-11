"""

Section 2: For Loops

Problem 2.1: Multiplication Table (Easy)
Write a program that prints the multiplication table for a given number (1 to 10).

Example output for number 5:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
Hint: Use for loop with range(1, 11) to iterate from 1 to 10. Multiply the number by loop variable i.

"""

table_num = int(input("Enter table number you want!"))

print("Multiplication Table\n")

print(f"Table {table_num}\n")

for num in range(1, 11):
    result = table_num * num
    
    print(f"{table_num} X {num} = {result}")