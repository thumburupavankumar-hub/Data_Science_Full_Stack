# Question 15: Find the longest word in "Python is a programming language"

word = "Python is a programming language"

split_word = word.split()

for i in split_word:
    len_word = max(split_word,key=len)
    
print(f"Longest word : {len_word}")