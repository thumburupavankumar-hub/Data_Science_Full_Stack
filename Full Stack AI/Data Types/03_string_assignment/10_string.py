# Question 10: Remove all vowels from "Computer Science"

word = "Computer Science"
vowels = "aeiou"
result = ""

for char in word:
    if char.lower() not in vowels:
        result += char
        
print(f"Removing all vowels : {result}")