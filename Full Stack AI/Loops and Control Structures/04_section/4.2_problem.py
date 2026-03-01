"""

Problem 4.2: Pattern Printing - Inverted Right Triangle (Easy)
Print the following pattern for n rows:

*****
****
***
**
*
(Example shown for n=5)

Hint: Outer loop for rows.
Inner loop prints stars from 1 to (n-i+1), where i is the row number.

"""

number = int(input("Enter a number: "))

for i in range(number, 0, -1):
    for j in range(i):
        print("*", end=" ")
    
    print()