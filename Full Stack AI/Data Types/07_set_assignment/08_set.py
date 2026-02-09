# Question 8: Create a set of vowels from string "hello world"

char = "hello world"
vowels = "aeiou"
vowels_set = set()

for c in char:
    if c in vowels:
        vowels_set.add(c)
print(f"Vowels set : {vowels_set}")