# Question 9: Find the greatest common divisor (GCD) of 48 and 36

a = 48
b = 36

while b != 0:
    a, b = b, a % b

print(a)