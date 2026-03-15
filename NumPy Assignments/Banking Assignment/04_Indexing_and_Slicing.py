# ### Question 3: Indexing and Slicing


# **Q3.1:** Extract the first row of `banking_data`

first_row = banking_data[0]

print(f"First row of banking data: {first_row}")

# output:

# First row of banking data: ['C101' '5200' '720' '15' '4']


# **Q3.2:** Extract the last row of `banking_data`

last_row = banking_data[-1]

print(f"Last row of banking data: {last_row}")

# output:

# Last row of banking data: ['C999' '7200' '705' '16' '6']


# **Q3.3:** Extract the Account_Balance column (column index 1)

ac_balance = banking_data[:,1]

print(f"Account balance column: {ac_balance}")

# output:

# Account balance column: ['5200' '8900' '1200' '15000' '4300' '9800' '2750' '11200' '3500' '7200']


# **Q3.4:** Extract the first 4 rows and first 3 columns

four_three = banking_data[:4,:3]

print(f"First 4 rows and first 3 columns: \n{four_three}")

# output:

# First 4 rows and first 3 columns: 
# [['C101' '5200' '720']
#  ['C205' '8900' '680']
#  ['C309' '1200' '610']
#  ['C412' '15000' '750']]


# **Q3.5:** Extract rows 3 to 7 (inclusive)

rows_3to7 = banking_data[3:8]

print(f"Rows 3 to 7: \n{rows_3to7}")

# output:

# Rows 3 to 7: 
# [['C412' '15000' '750' '25' '10']
#  ['C587' '4300' '690' '12' '3']
#  ['C623' '9800' '710' '18' '7']
#  ['C744' '2750' '640' '9' '4']
#  ['C856' '11200' '770' '30' '12']]