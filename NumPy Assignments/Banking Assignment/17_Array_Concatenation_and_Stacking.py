# ### Question 16: Array Concatenation and Stacking


# **Q16.1:** Concatenate two arrays horizontally using `np.hstack()`

interest = np.array([100, 200, 50, 300, 120, 220, 80, 350, 90, 180])
result = np.hstack((banking_data, interest.reshape(-1,1)))

print(f"Concatenated two arrays horizontally: \n{result}")

# output:

# Concatenated two arrays horizontally: 
# [['C101' '5200' '720' '15' '4' '100']
#  ['C205' '8900' '680' '20' '6' '200']
#  ['C309' '1200' '610' '8' '2' '50']
#  ['C412' '15000' '750' '25' '10' '300']
#  ['C587' '4300' '690' '12' '3' '120']
#  ['C623' '9800' '710' '18' '7' '220']
#  ['C744' '2750' '640' '9' '4' '80']
#  ['C856' '11200' '770' '30' '12' '350']
#  ['C912' '3500' '660' '11' '5' '90']
#  ['C999' '7200' '705' '16' '6' '180']]


# **Q16.2:** Concatenate two arrays vertically using `np.vstack()`

table1 = banking_data[:5]   # First 5 rows
table2 = banking_data[5:]   # Last 5 rows
result = np.vstack((part1, part2))

print(f"Concatenated two arrays vertically: \n{result}")

# output:

# Concatenated two arrays vertically: 
# [['C101' '5200' '720' '15' '4']
#  ['C205' '8900' '680' '20' '6']
#  ['C309' '1200' '610' '8' '2']
#  ['C412' '15000' '750' '25' '10']
#  ['C587' '4300' '690' '12' '3']
#  ['C623' '9800' '710' '18' '7']
#  ['C744' '2750' '640' '9' '4']
#  ['C856' '11200' '770' '30' '12']
#  ['C912' '3500' '660' '11' '5']
#  ['C999' '7200' '705' '16' '6']]


# **Q16.3:** Concatenate arrays along a specific axis using `np.concatenate()`

table1 = banking_data[:5]
table2 = banking_data[5:]
result = np.concatenate((table1, table2), axis= 0)

print(f"Concatenated arrays along a specific axis using `np.concatenate()`: \n{result}")

# output:

# Concatenated arrays along a specific axis using `np.concatenate()`: 
# [['C101' '5200' '720' '15' '4']
#  ['C205' '8900' '680' '20' '6']
#  ['C309' '1200' '610' '8' '2']
#  ['C412' '15000' '750' '25' '10']
#  ['C587' '4300' '690' '12' '3']
#  ['C623' '9800' '710' '18' '7']
#  ['C744' '2750' '640' '9' '4']
#  ['C856' '11200' '770' '30' '12']
#  ['C912' '3500' '660' '11' '5']
#  ['C999' '7200' '705' '16' '6']]


# **Q16.4:** Stack arrays depth-wise using `np.dstack()`

account_balance = banking_data[:,1].astype(float)
credit_score = banking_data[:,2].astype(float)
depth_wise_stack = np.dstack((account_balance, credit_score))

print(f"Stack arrays depth-wise: \n{depth_wise_stack}")
print(f"Shape: \n{depth_wise_stack.shape}")

# output:

# Stack arrays depth-wise: 
# [[[ 5200.   720.]
#   [ 8900.   680.]
#   [ 1200.   610.]
#   [15000.   750.]
#   [ 4300.   690.]
#   [ 9800.   710.]
#   [ 2750.   640.]
#   [11200.   770.]
#   [ 3500.   660.]
#   [ 7200.   705.]]]
# Shape: 
# (1, 10, 2)


# **Q16.5:** Create a column stack using `np.column_stack()`

account_balance = banking_data[:,1].astype(float)
credit_score = banking_data[:,2].astype(float)
column_stack = np.dstack((account_balance, credit_score))

print(f"Column stack: \n{column_stack}")
print(f"Shape: \n{column_stack.shape}")

# output:

# Column stack: 
# [[[ 5200.   720.]
#   [ 8900.   680.]
#   [ 1200.   610.]
#   [15000.   750.]
#   [ 4300.   690.]
#   [ 9800.   710.]
#   [ 2750.   640.]
#   [11200.   770.]
#   [ 3500.   660.]
#   [ 7200.   705.]]]
# Shape: 
# (1, 10, 2)