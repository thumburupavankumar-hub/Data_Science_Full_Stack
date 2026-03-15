# ### Question 6: Array Reshaping and Manipulation


# **Q6.1:** Reshape the `banking_data` to 5 rows × 10 columns

reshape_data = banking_data.reshape(5,10)
print(f"Reshaped data: \n{reshape_data}")

# output:

# Reshaped data: 
# [['C101' '5200' '720' '15' '4' 'C205' '8900' '680' '20' '6']
#  ['C309' '1200' '610' '8' '2' 'C412' '15000' '750' '25' '10']
#  ['C587' '4300' '690' '12' '3' 'C623' '9800' '710' '18' '7']
#  ['C744' '2750' '640' '9' '4' 'C856' '11200' '770' '30' '12']
#  ['C912' '3500' '660' '11' '5' 'C999' '7200' '705' '16' '6']]


# **Q6.2:** Flatten the `banking_data` to a 1D array

flatten_array = banking_data.flatten()

print(f"1D array of banking data: \n{flatten_array}")

# output:

# 1D array of banking data: 
# ['C101' '5200' '720' '15' '4' 'C205' '8900' '680' '20' '6' 'C309' '1200'
#  '610' '8' '2' 'C412' '15000' '750' '25' '10' 'C587' '4300' '690' '12' '3'
#  'C623' '9800' '710' '18' '7' 'C744' '2750' '640' '9' '4' 'C856' '11200'
#  '770' '30' '12' 'C912' '3500' '660' '11' '5' 'C999' '7200' '705' '16' '6']


# **Q6.3:** Transpose the `banking_data`

transpose_data = banking_data.transpose()

print(f"Transpose data: \n{transpose_data}")

# output:

# Transpose data: 
# [['C101' 'C205' 'C309' 'C412' 'C587' 'C623' 'C744' 'C856' 'C912' 'C999']
#  ['5200' '8900' '1200' '15000' '4300' '9800' '2750' '11200' '3500' '7200']
#  ['720' '680' '610' '750' '690' '710' '640' '770' '660' '705']
#  ['15' '20' '8' '25' '12' '18' '9' '30' '11' '16']
#  ['4' '6' '2' '10' '3' '7' '4' '12' '5' '6']]


# **Q6.4:** Split the `banking_data` into 2 equal parts vertically

vertical_split = np.vsplit(banking_data,2)
print(f"Banking data into 2 equal parts vertically: \n{vertical_split}")

# output:

# Banking data into 2 equal parts vertically: 
# [array([['C101', '5200', '720', '15', '4'],
#        ['C205', '8900', '680', '20', '6'],
#        ['C309', '1200', '610', '8', '2'],
#        ['C412', '15000', '750', '25', '10'],
#        ['C587', '4300', '690', '12', '3']], dtype='<U21'), array([['C623', '9800', '710', '18', '7'],
#        ['C744', '2750', '640', '9', '4'],
#        ['C856', '11200', '770', '30', '12'],
#        ['C912', '3500', '660', '11', '5'],
#        ['C999', '7200', '705', '16', '6']], dtype='<U21')]


# **Q6.5:** Split the `banking_data` into 2 equal parts horizontally

horizontal_split = np.hsplit(banking_data, [3])

print(f"Banking_data into 2 equal parts horizontally: \n{horizontal_split}")    # The number 3 means the split happens BEFORE column index 3.

# output:

# Banking_data into 2 equal parts horizontally: 
# [array([['C101', '5200', '720'],
#        ['C205', '8900', '680'],
#        ['C309', '1200', '610'],
#        ['C412', '15000', '750'],
#        ['C587', '4300', '690'],
#        ['C623', '9800', '710'],
#        ['C744', '2750', '640'],
#        ['C856', '11200', '770'],
#        ['C912', '3500', '660'],
#        ['C999', '7200', '705']], dtype='<U21'), array([['15', '4'],
#        ['20', '6'],
#        ['8', '2'],
#        ['25', '10'],
#        ['12', '3'],
#        ['18', '7'],
#        ['9', '4'],
#        ['30', '12'],
#        ['11', '5'],
#        ['16', '6']], dtype='<U21')]