# ### Question 7: Logical Operations and Filtering


# **Q7.1:** Find customers with account balance greater than $100,00

salary = banking_data[:,1].astype(float)
high_bal_customers = banking_data[salary > 10000]

print(f"Customers with account balance greater than $100,00: \n{high_bal_customers}")

# output:

# Customers with account balance greater than $100,00: 
# [['C412' '15000' '750' '25' '10']
#  ['C856' '11200' '770' '30' '12']]


# **Q7.2:** Find customers with credit score greater than 800

credit_score = banking_data[:,2].astype(float)
high_score = banking_data[credit_score > 800]

print(f"Customers with credit score greater than 800: \n{high_score}")

# output:

# Customers with credit score greater than 800: 
# []


# **Q7.3:** Find customers with transaction count greater than 50 AND credit score less than 750

transaction_count = banking_data[:,3].astype(float)
credit_score = banking_data[:,2].astype(float)

customer = banking_data[(transaction_count > 50)  & (credit_score < 750)]

print(f"Customers with transaction count greater than 50 AND credit score less than 750: \n{customer}")

# output:

# Customers with transaction count greater than 50 AND credit score less than 750: 
# []


# **Q7.4:** Count how many customers have account balance between $10,000 and $100,000

account_balance = banking_data[:,1].astype(float)
customer = banking_data[(account_balance >= 10000) & (account_balance <= 100000)]

print(f"Customers have account balance between $10,000 and $100,000: \n{len(customer)}")

# output:

# Customers have account balance between $10,000 and $100,000: 
# 2


# **Q7.5:** Find the index of the customer with the highest credit score

credit_score = banking_data[:,3].astype(float)
highest_score_index = credit_score.argmax()

print(f"Index of the customer with the highest credit score: \n{highest_score_index}")

# output:

# Index of the customer with the highest credit score: 
# 7