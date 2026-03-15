# ### Question 2: Array Attributes and Information


# **Q2.1:** What is the shape of the `banking_data` array?

shape_data = banking_data.shape

print(f"Shape of the data: {shape_data}")

# output:

# Shape of the data: (10, 5)


# **Q2.2:** What is the data type of the `banking_data` array?

data_type = banking_data.dtype

print(f"Data Type: {data_type}")

# output:

# Data Type: <U21


# **Q2.3:** What is the size (total number of elements) of the `banking_data` array?

size_data = banking_data.size

print(f"Size of the data: {size_data}")

# output:

# Size of the data: 50


# **Q2.4:** What is the number of dimensions of the `banking_data` array?

dimensions = banking_data.ndim

print(f"Dimensions of bnaking data: {dimensions}")

# output:

# Dimensions of bnaking data: 2


# **Q2.5:** What is the memory size of the `banking_data` array in bytes?

memory_size = banking_data.nbytes

print(f"Memory size of banking data: {memory_size} bytes.")

# output:

# Memory size of banking data: 4200 bytes.