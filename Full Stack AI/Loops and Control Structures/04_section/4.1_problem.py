"""

Problem 4.1: Pattern Printing - Right Triangle (Easy)
Print the following pattern for n rows:

*
**
***
****
*****
(Example shown for n=5)

Hint: Use nested loops: outer loop for rows (i from 1 to n), inner loop for columns (j from 1 to i).
Print * in inner loop.

"""

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print('*',end= ' ')
        
    print()