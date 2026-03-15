# ### Question 5: Statistical Functions


# **Q5.1:** Find the minimum and maximum account balances

min_balalnce = np.min(banking_data[:,1].astype(float))
max_balalnce = np.max(banking_data[:,1].astype(float))

print(f"Minimum account balance: {min_balalnce:.2f}")
print(f"Maximum account balance: {max_balalnce:.2f}")

# output:

# Minimum account balance: 1200.00
# Maximum account balance: 15000.00

# **Q5.2:** Find the minimum and maximum credit scores

min_score = np.min(banking_data[:,2].astype(float))
max_score = np.max(banking_data[:,2].astype(float))

print(f"Minimum credit score: {min_score}")
print(f"Maximum credit score: {max_score}")

# output:

# Minimum credit score: 610.0
# Maximum credit score: 770.0

# **Q5.3:** Calculate the percentile values for account balances (25th, 50th, 75th)

percentile_value = np.percentile(banking_data[:,1].astype(float),[25,50,75])

print(f"25th percentile value of account balance: {percentile_value[0]}")
print(f"50th percentile value of account balance: {percentile_value[1]}")
print(f"75th percentile value of account balance: {percentile_value[2]}")

# output:

# 25th percentile value of account balance: 3700.0
# 50th percentile value of account balance: 6200.0
# 75th percentile value of account balance: 9575.0


# **Q5.4:** Calculate the correlation between account balance and credit score

correlation = np.corrcoef(banking_data[:,1].astype(float),banking_data[:,2].astype(float))[0,1]

print(f"Correlation between account balance and credit score: {correlation}")

# output:

# Correlation between account balance and credit score: 0.8399965422784104

# **Q5.5:** Calculate the covariance between account balance and credit score

covariance = np.cov(banking_data[:,1].astype(float),banking_data[:,2].astype(float))[0,1]

print(f"Covariance between account balance and credit score: {covariance} ")

# output:

# Covariance between account balance and credit score: 176313.88888888888 