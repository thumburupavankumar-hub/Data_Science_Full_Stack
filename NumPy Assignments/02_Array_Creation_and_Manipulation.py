# ### Question 1: Array Creation and Manipulation

# **Q1.1:** Create a 4x4 identity matrix using `np.eye()`

identity_matrix = np.eye(4)

print(f"Identity matrix: \n{identity_matrix}")

# output:

"""
Identity matrix: 
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
 """


# **Q1.2:** Create an array of 8 zeros using `np.zeros()`

zeros_array = np.zeros(8)

print(f"Zeros array: {zeros_array}")

# output:

# Zeros array: [0. 0. 0. 0. 0. 0. 0. 0.]


# **Q1.3:** Create an array of 6 ones using `np.ones()`

ones_array = np.ones(6)

print(f"Ones array: {ones_array}")

# output:

# Ones array: [1. 1. 1. 1. 1. 1.]


# **Q1.4:** Create an array with values from 0 to 15 using `np.arange()`

range_array = np.arange(0,16)

print(f"Range of 0 to 15: {range_array}")

# output:

# Range of 0 to 15: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]


# **Q1.5:** Create an array with 8 evenly spaced values from 0 to 100 using `np.linspace()`

linspaces = np.linspace(0,101,8)

print(linspaces)

# output:

# [  0.          14.42857143  28.85714286  43.28571429  57.71428571
#   72.14285714  86.57142857 101.        ]