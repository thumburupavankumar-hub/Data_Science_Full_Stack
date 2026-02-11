"""

Problem 1.3: Triangle Type Identifier (Medium)
Write a program that takes three sides of a triangle as input and determines:

Whether the three sides can form a valid triangle (sum of any two sides must be greater than the third side)
If valid, classify the triangle as:
Equilateral (all three sides equal)
Isosceles (exactly two sides equal)
Scalene (no sides equal)
Hint: First check: (a+b>c) and (b+c>a) and (a+c>b). Then use == to compare sides: if all three equal, it's equilateral; if any two equal, it's isosceles; otherwise scalene.

"""

print("Triangle Type Identifier")

s1 = int(input("Enter first side value of triangle : "))
s2 = int(input("Enter second side value of triangle : "))
s3 = int(input("Enter third side value of triangle : "))

if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    
    if s1 == s2 == s3:
        print("Type of triangle : Equilateral")
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print("Type of triange : Isosceles")
    else:
        print("Type of triange : Scalene")
else:
    print("Not a valid triangle")