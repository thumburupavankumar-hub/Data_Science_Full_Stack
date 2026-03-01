"""

Problem 4.6: Diamond Pattern (Hard)
Print a diamond pattern for n rows (n should be odd):

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
(Example shown for n=9)

Hint: Print pyramid (upper half) for rows 1 to (n+1)//2, then print inverted pyramid (lower half) for remaining rows.

"""

number = int(input("Enter an odd number: "))

mid = (number + 1) // 2   # Middle row

# Upper half (including middle)
for i in range(1, mid + 1):
    print(" " * (mid - i) + "*" * (2 * i - 1))

# Lower half
for i in range(mid - 1, 0, -1):
    print(" " * (mid - i) + "*" * (2 * i - 1))