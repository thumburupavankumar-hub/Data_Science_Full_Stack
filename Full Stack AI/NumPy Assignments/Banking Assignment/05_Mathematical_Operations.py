# ### Question 4: Mathematical Operations


# **Q4.1:** Calculate the sum of all account balances

total_balance = np.sum(banking_data[:,1].astype(float))

print(f"Total account balance: {total_balance} ")

# output:

# Total account balance: 69050.0 


# **Q4.2:** Calculate the mean account balance

avg_balance = np.mean(banking_data[:,1].astype(float))

print(f"Average of the account balance: {avg_balance:.2f}")

# output:

# Average of the account balance: 6905.00


# **Q4.3:** Calculate the standard deviation of account balances

std_balance = np.std(banking_data[:,1].astype(float))

print(f"Standard deviation of the account balance: {std_balance:.2f}")

# output:

# Standard deviation of the account balance: 4092.95


# **Q4.4:** Calculate the variance of account balances

variances = np.var(banking_data[:,1].astype(float))

print(f"Variance of the account balance: {variances:.2f}") 

# output:

# Variance of the account balance: 16752225.00


# **Q4.5:** Calculate the median account balance

median_balance = np.median(banking_data[:,1].astype(float))

print(f"Median value of the account balance: {median_balance:.2f}")

# output:

# Median value of the account balance: 6200.00