# ### Question 10: Advanced Operations


# **Q10.1:** Calculate the cumulative sum of account balances

account_balance = banking_data[:,1].astype(float)
cumulative_sum = np.cumsum(account_balance)

print(f"Cumulative sum of account balances: \n{cumulative_sum}")

# output:

# Cumulative sum of account balances: 
# [ 5200. 14100. 15300. 30300. 34600. 44400. 47150. 58350. 61850. 69050.]


# **Q10.2:** Calculate the cumulative product of transaction counts

transaction_count = banking_data[:,3].astype(float)
cumulative_product = np.cumprod(transaction_count)

print(f"Cumulative product of transaction counts: \n{cumulative_product}")

# output:

# Cumulative product of transaction counts: 
# [1.500000e+01 3.000000e+02 2.400000e+03 6.000000e+04 7.200000e+05
#  1.296000e+07 1.166400e+08 3.499200e+09 3.849120e+10 6.158592e+11]


# **Q10.3:** Calculate the difference between consecutive account balances

account_balance = banking_data[:,1].astype(float)
consecutive = np.diff(account_balance)

print(f"Difference between consecutive account balances: \n{consecutive}")

# output:

# Difference between consecutive account balances: 
# [  3700.  -7700.  13800. -10700.   5500.  -7050.   8450.  -7700.   3700.]


# **Q10.4:** Calculate the gradient of account balances

account_balance = banking_data[:,1].astype(float)
gradient = np.gradient(account_balance)

print(f"Gradient of account balances: \n{gradient}")

# output:

# Gradient of account balances: 
# [ 3700. -2000.  3050.  1550. -2600.  -775.   700.   375. -2000.  3700.]


# **Q10.5:** Calculate the histogram of account balances with 5 bins

account_balance = banking_data[:,1].astype(float)
histogram = np.histogram(account_balance, 5)

print(f"Histogram of account balances with 5 bins: \n{histogram}")

# output:

# Histogram of account balances with 5 bins: 
# (array([3, 2, 2, 2, 1]), array([ 1200.,  3960.,  6720.,  9480., 12240., 15000.]))