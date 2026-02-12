# Question 11: Find the most frequent character in "mississippi"

word = "mississippi"

frequency = {}

for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
        
max_freq = max(frequency.values())
most_freq =[char for char, count in frequency.items() if count == max_freq]

print(f"Most frequent character : {most_freq}")