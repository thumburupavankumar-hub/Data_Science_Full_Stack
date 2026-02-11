"""

Problem 2.6: Count Digits in a Number (Easy)
Write a program that counts the number of digits in a given integer.

Example: 12345 has 5 digits

Hint: Convert number to string and use len(), or keep dividing by 10 until number becomes 0, counting each division.

"""

print("Count Digits in a Number\n")

number = int(input("Enter number : "))

count = 0

for num in str(number):
    count += 1
    
print(f"Digits in {number} : {int(count)}")