"""

Problem 3.5: Armstrong Number (Hard)
Write a program to check if a number is an Armstrong number (also called Narcissistic number).

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Examples:

153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 (Armstrong number)
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 (Armstrong number)
Hint: First count digits (power). Store original. Extract each digit, raise to power, add to sum. Compare sum with original.

"""

number1 = int(input("Enter number: "))

original1 = number1
temp = number1
count = 0
total = 0

# Count digits
while temp > 0:
    count += 1
    temp = temp // 10
    
temp = original1     # Reset temp to original number

# Calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10
    total += digit ** count
    temp = temp // 10
    
# Compare
if total == original1:
    print(f"{original1} is an Armstrong number.")
else:
    print(f"{original1} is Not an Armstrong number.")