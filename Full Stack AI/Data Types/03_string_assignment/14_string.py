# Question 14: Count consonants in "Hello World"

word = "Hello World"
vowels = "aeiou"

count = 0

for i in word.lower():
    if i not in vowels:
        count+=1
        
print(f"Constrants : {count}")