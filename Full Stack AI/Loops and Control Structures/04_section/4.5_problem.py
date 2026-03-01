"""

Problem 4.5: Multiplication Table Grid (Medium)
Print a multiplication table grid from 1 to n.

Example for n=5:

1   2   3   4   5
2   4   6   8  10
3   6   9  12  15
4   8  12  16  20
5  10  15  20  25
Hint: Nested loops: for i in range(1, n+1) and for j in range(1, n+1).
Print i*j with proper spacing.

"""

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(i * j, end= "\t")
        
    print()