# Question 9: Count frequency of each character in string "hello"

string = "hello"
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
        
print(frequency)

# Question 9: Count frequency of each character in string "hello"

string = "hello"
frequency = {}

for char in string:
    frequency[char] = frequency.get(char, 0) + 1
    
print(frequency)