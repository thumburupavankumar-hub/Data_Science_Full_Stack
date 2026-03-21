# ### Question 12: Linear Algebra Operations


# **Q12.1:** Calculate the dot product of account balance and credit score columns

account_balance = banking_data[:,1].astype(float)
credit_score = banking_data[:,2].astype(float)

dot_product = np.dot(account_balance,credit_score)

print(f"Dot product of account balance and credit score columns: \n{dot_product}")

# output:

# Dot product of account balance and credit score columns: 
# 49473000.0


# **Q12.2:** Calculate the cross product of first two rows

first_row = banking_data[0,1:4].astype(float)
second_row = banking_data[1,1:4].astype(float)
cross_product = np.cross(first_row,second_row)

print(f"Cross product of first two rows: \n{cross_product}")

# output:

# Cross product of first two rows: 
# [ 1.330e+03  2.720e+04 -1.797e+06]


# **Q12.3:** Calculate the norm (magnitude) of the account balance column

account_balance = banking_data[:,1].astype(float)
norm_magnitude = np.linalg.norm(account_balance)

print(f"Norm (magnitude) of the account balance column: \n{norm_magnitude}")

# output:

# Norm (magnitude) of the account balance column: 
# 25383.311446696625


# **Q12.4:** Create a 3x3 matrix and calculate its determinant

matrix = np.random.randint(0,100,(3,3))
determinant = np.linalg.det(matrix)

print(f"3x3 matrix and determinant: \n{determinant}")


# output:

# 3x3 matrix and determinant: 
# -152814.99999999988


# **Q12.5:** Calculate the inverse of the 3x3 matrix

matrix = np.random.randint(0,100,(3,3))
inverse = np.linalg.inv(matrix)

print(f"Inverse of the 3x3 matrix: \n{inverse}")

# output:

# Inverse of the 3x3 matrix: 
# [[ 0.09905956  0.17366771 -0.1721451 ]
#  [-0.00846395 -0.0369906   0.03640842]
#  [-0.09749216 -0.12978056  0.14952978]]