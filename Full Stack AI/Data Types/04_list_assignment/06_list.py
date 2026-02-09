# Question 6: Create a list of first 15 Fibonacci numbers

n_terms = 15
n1, n2 = 0, 1
fibonacci = []

for _ in range(n_terms):
    fibonacci.append(n1)
    n1, n2 = n2, n1 + n2

print(f"Fibonacci sequence : {fibonacci}")