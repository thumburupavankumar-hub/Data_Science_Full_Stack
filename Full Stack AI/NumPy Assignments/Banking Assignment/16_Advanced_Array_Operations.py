# ### Question 15: Advanced Array Operations


# **Q15.1:** Apply a function to calculate 5% interest on all account balances

account_balance = banking_data[:,1].astype(float)
interest = account_balance * 0.05

print(f"5% interest on all account balances: \n{interest}")

# output:

# 5% interest on all account balances: 
# [360.  490.  215.  175.  260.  137.5 445.  750.  560.   60. ]


# **Q15.2:** Use `np.where` to categorize customers by balance ranges

account_balance = banking_data[:,1].astype(float)
category = np.where(account_balance < 3000, 'Low',np.where(account_balance < 8000, 'Medium','High'))    # Here 'High' is else condition.

print(f"Customers by balance ranges: \n{category}")

# output:

# Customers by balance ranges: 
# ['Medium' 'High' 'Medium' 'Medium' 'Medium' 'Low' 'High' 'High' 'High'
#  'Low']


# **Q15.3:** Use `np.select` to categorize customers by credit score ranges

credit_score = banking_data[:,2].astype(float)
conditions = [
    credit_score < 650,
    (credit_score >= 650) & (credit_score < 700),
    (credit_score >= 700) & (credit_score < 750),
    credit_score >= 750
]
choices = ["Low", "Medium", "Good", "Exellent"]
category = np.select(conditions, choices, default='unknown')    # Here default='unknown' is used. Because, default= 0 is int. So dtype mismatches.

print(f"Categorized customers by balance ranges: \n{category}")

# output:

# Categorized customers by balance ranges: 
# ['Good' 'Good' 'Medium' 'Medium' 'Good' 'Low' 'Medium' 'Exellent'
#  'Exellent' 'Low']


# **Q15.4:** Use `np.piecewise` to apply different interest rates based on balance

account_balance = banking_data[:,1].astype(float)
interest = np.piecewise(
    account_balance,
    [account_balance < 3000,
     (account_balance >= 3000) & (account_balance <= 8000),
     account_balance > 8000],
    [lambda x: x * 0.02,
    lambda x: x * 0.04,
    lambda x: x * 0.06,]
)

print(f"Interest rates based on balance: \n{interest}")

# output:

# Interest rates based on balance: 
# [208. 534.  24. 900. 172. 588.  55. 672. 140. 288.]


# **Q15.5:** Use `np.apply_along_axis` to calculate the sum of each row

account_balance = banking_data[:,1:].astype(float)
row_sum = np.apply_along_axis(np.sum, axis=1, arr= account_balance)

print(f"Sum of each row: \n{row_sum}")

# output:

# Sum of each row: 
# [ 5939.  9606.  1820. 15785.  5005. 10535.  3403. 12012.  4176.  7927.]