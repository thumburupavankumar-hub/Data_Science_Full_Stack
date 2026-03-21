# ### Question 13: String Operations


# **Q13.1:** Convert all customer IDs to strings

customer_id = banking_data[:,0].astype(str)

print(f"All customer IDs to strings: \n{customer_id}")
print(f"Data type: {customer_id.dtype}")

# output:

# All customer IDs to strings: 
# ['C999' 'C623' 'C587' 'C912' 'C101' 'C744' 'C205' 'C412' 'C856' 'C309']
# Data type: <U21


# **Q13.2:** Check if any customer ID contains '100'

customer_id = banking_data[:,0]
check = np.any(['100' in id for id in customer_id])

if check:
    print("Yes!")
else:
    print("No!")

# output:

# No!


# **Q13.3:** Convert all customer IDs to uppercase (if they were strings)

customer_id = banking_data[:,0]
uppercase = np.char.upper(customer_id)

print(f"All customer IDs to uppercase: \n{uppercase}")

# output:

# All customer IDs to uppercase: 
# ['C999' 'C623' 'C587' 'C912' 'C101' 'C744' 'C205' 'C412' 'C856' 'C309']


# **Q13.4:** Count the length of each customer ID string

customer_id = banking_data[:,0]
length_id = np.char.str_len(customer_id)

print(f"Length of each customer ID string: \n{length_id}")

# output:

# Length of each customer ID string: 
# [4 4 4 4 4 4 4 4 4 4]


# **Q13.5:** Replace '100' with 'CUST' in customer IDs

customer_id = banking_data[:,0]
replace = np.char.replace(customer_id,'100','CUST')

print(f"Replaced '100' with 'CUST' in customer IDs: \n{replace}")

# output:

# Replaced '100' with 'CUST' in customer IDs: 
# ['C999' 'C623' 'C587' 'C912' 'C101' 'C744' 'C205' 'C412' 'C856' 'C309']