"""

Problem 4.4: Pattern Printing - Number Pattern (Medium)
Print the following number pattern for n rows:

1
12
123
1234
12345
(Example shown for n=5)

Hint: Similar to Problem 4.1, but print j (column number) instead of *.

"""

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end= " ")
        
    print()