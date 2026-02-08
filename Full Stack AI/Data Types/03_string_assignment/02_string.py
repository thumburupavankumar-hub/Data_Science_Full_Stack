# Question 2: Check if "racecar" is a palindrome

word = input("Enter a word: ").lower()
rev = word[::-1]

if word == rev:
    print("It's Palindrome")
else:
    print("Not a Palindrome")