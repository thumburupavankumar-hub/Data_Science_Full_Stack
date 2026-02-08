# Question 7: Check if "python" is in "Python Programming Language"

word = "Python Programming Language"
char = "python"

if char.lower() in word.lower():
    print(f"{char} is in {word}")
else:
    print(f"{char} is not in {word}")