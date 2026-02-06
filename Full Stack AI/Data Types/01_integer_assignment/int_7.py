# Question 7: Find the factorial of 8

num = int(input("Enter a number: "))
factorial = 1

for i in range (1, num+1):
    factorial *= i
    
print (factorial)