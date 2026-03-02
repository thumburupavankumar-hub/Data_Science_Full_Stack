"""

Problem 5.2: Skip Multiples (Easy)
Write a program that prints all numbers from 1 to 50, but skips (doesn't print) numbers that are multiples of 3.
Use the continue statement.

Hint: Loop from 1 to 50. If i%3==0, use continue to skip to next iteration. Otherwise print i.

"""

for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i, end= ",")