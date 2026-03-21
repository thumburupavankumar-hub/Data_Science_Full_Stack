# ### Question 9: Mathematical Functions


# **Q9.1:** Calculate the absolute values of all elements

numeric_data = banking_data[:,1:].astype(float)
absolute_value = np.abs(numeric_data)

print(f"Absolute values of all elements: \n{absolute_value}")

# output:

# Absolute values of all elements: 
# [[5.20e+03 7.20e+02 1.50e+01 4.00e+00]
#  [8.90e+03 6.80e+02 2.00e+01 6.00e+00]
#  [1.20e+03 6.10e+02 8.00e+00 2.00e+00]
#  [1.50e+04 7.50e+02 2.50e+01 1.00e+01]
#  [4.30e+03 6.90e+02 1.20e+01 3.00e+00]
#  [9.80e+03 7.10e+02 1.80e+01 7.00e+00]
#  [2.75e+03 6.40e+02 9.00e+00 4.00e+00]
#  [1.12e+04 7.70e+02 3.00e+01 1.20e+01]
#  [3.50e+03 6.60e+02 1.10e+01 5.00e+00]
#  [7.20e+03 7.05e+02 1.60e+01 6.00e+00]]


# **Q9.2:** Calculate the square root of all account balances

account_balance = banking_data[:,1].astype(float)
square_root = np.sqrt(account_balance)

print(f"Square root of all account balances: \n{square_root}")

# output:

# Square root of all account balances: 
# [ 72.11102551  94.33981132  34.64101615 122.47448714  65.57438524
#   98.99494937  52.44044241 105.83005244  59.16079783  84.85281374]


# **Q9.3:** Calculate the square of all credit scores

credit_score = banking_data[:,2].astype(float)
square = credit_score ** 2

print(f"Square of all credit scores: \n{square}")

# output:

# Square of all credit scores: 
# [518400. 462400. 372100. 562500. 476100. 504100. 409600. 592900. 435600.
#  497025.]


# **Q9.4:** Calculate the exponential of all transaction counts

transaction = banking_data[:,3].astype(float)
exponential = np.exp(transaction)

print(f"Exponential of all transaction counts: \n{exponential}")

# output:

# Exponential of all transaction counts: 
# [3.26901737e+06 4.85165195e+08 2.98095799e+03 7.20048993e+10
#  1.62754791e+05 6.56599691e+07 8.10308393e+03 1.06864746e+13
#  5.98741417e+04 8.88611052e+06]


# **Q9.5:** Calculate the natural logarithm of all account balances

account_balance = banking_data[:,1].astype(float)
natural_log = np.log(account_balance)

print(f"Natural logarithm of all account balances: \n{natural_log}")

# output:

# Natural logarithm of all account balances: 
# [8.5564139  9.09380656 7.09007684 9.61580548 8.3663703  9.19013766
#  7.91935619 9.32366906 8.16051825 8.88183631]