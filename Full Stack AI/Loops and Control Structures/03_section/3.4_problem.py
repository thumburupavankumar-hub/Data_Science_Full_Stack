"""

Problem 3.4: Palindrome Checker (Medium)
Write a program to check if a given number is a palindrome or not.

A palindrome number reads the same forwards and backwards.

Examples: 121, 12321, 1331 are palindromes

Hint: Store original number, reverse it (like Problem 3.1), then compare original with reversed number.

"""

number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10     # Get last digit
    reverse = reverse * 10 + digit
    number = number // 10   # Remove last digit
    
# Compare original and reversed number
if original == reverse:
    print(f"{original} is Palindrome.")
else:
    print(f"{original} is Not a Palindrome.")