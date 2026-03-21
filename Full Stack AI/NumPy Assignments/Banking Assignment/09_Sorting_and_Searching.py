# ### Question 8: Sorting and Searching


# **Q8.1:** Sort the `banking_data` by account balance (ascending)

balance = banking_data[:,1].astype(float)
asc_order = banking_data[balance.argsort()]

print(f"Sort the `banking_data` by account balance (ascending): \n{asc_order}")

# output:

# Sort the `banking_data` by account balance (ascending): 
# [['C309' '1200' '610' '8' '2']
#  ['C744' '2750' '640' '9' '4']
#  ['C912' '3500' '660' '11' '5']
#  ['C587' '4300' '690' '12' '3']
#  ['C101' '5200' '720' '15' '4']
#  ['C999' '7200' '705' '16' '6']
#  ['C205' '8900' '680' '20' '6']
#  ['C623' '9800' '710' '18' '7']
#  ['C856' '11200' '770' '30' '12']
#  ['C412' '15000' '750' '25' '10']]


# **Q8.2:** Sort the `banking_data` by credit score (descending)

credit_score = banking_data[:,2].astype(float)
score_desc = banking_data[credit_score.argsort()[::-1]]

print(f"Sort the `banking_data` by credit score (descending): \n{score_desc}")

# output:

# Sort the `banking_data` by credit score (descending): 
# [['C856' '11200' '770' '30' '12']
#  ['C412' '15000' '750' '25' '10']
#  ['C101' '5200' '720' '15' '4']
#  ['C623' '9800' '710' '18' '7']
#  ['C999' '7200' '705' '16' '6']
#  ['C587' '4300' '690' '12' '3']
#  ['C205' '8900' '680' '20' '6']
#  ['C912' '3500' '660' '11' '5']
#  ['C744' '2750' '640' '9' '4']
#  ['C309' '1200' '610' '8' '2']]


# **Q8.3:** Find the indices that would sort the array by years active

years_acv = banking_data[:,4].astype(float)
indices = years_acv.argsort()

print(f"Indices that would sort the array by years active: \n{indices}")

# output:

# Indices that would sort the array by years active: 
# [2 4 6 0 8 1 9 5 3 7]


# **Q8.4:** Find the customer with the second highest account balance

account_balance = banking_data[:,1].astype(float)
sorted_balance = np.argsort(account_balance)
second_max = sorted_balance[-2]
customer_id = banking_data[second_max,0]
balance = account_balance[second_max]

print(f"{customer_id} with the second highest account balance: \n{balance}")

# output:

# C856 with the second highest account balance: 
# 11200.0


# **Q8.5:** Find the customer with the lowest transaction count

transaction = banking_data[:,3].astype(float)
lowest_count = np.argmin(transaction)
customer_id = banking_data[lowest_count,0]
lowest_transaction = transaction[lowest_count]

print(f"{customer_id} with the lowest transaction count: \n{lowest_transaction}")

# output:

# C309 with the lowest transaction count: 
# 8.0