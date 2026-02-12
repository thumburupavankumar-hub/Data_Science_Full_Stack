# Question 12: Check if two strings are anagrams: "listen" and "silent"

word1 = "listen"
word2 = "silent"

if sorted(word1)==sorted(word2):
    print("Anagrams")
else:
    print("Not a Anagram")