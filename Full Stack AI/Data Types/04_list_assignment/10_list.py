# Question 10: Create a list of prime numbers between 1 and 50

prime_num = []

for i in range(2,51):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_num.append(i)
        
print(f"List of prime numbers : {prime_num}")