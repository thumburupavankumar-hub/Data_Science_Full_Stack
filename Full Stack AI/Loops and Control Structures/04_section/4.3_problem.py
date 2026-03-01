"""

Problem 4.3: Pattern Printing - Pyramid (Medium)
Print the following pyramid pattern for n rows:

    *
   ***
  *****
 *******
*********
(Example shown for n=5)

Hint: For row i: print (n-i) spaces, then print (2*i-1) stars.
Use nested loops or string multiplication.

"""

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    
    for j in range(1, number - i + 1):
        print(" ", end= " ")
        
    for k in range(1, 2 * i):
        print("*", end= " ")
        
    print()