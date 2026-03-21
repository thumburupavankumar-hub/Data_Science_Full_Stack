# ### Question 14: Date and Time Operations


# **Q14.1:** Convert years active to months

years_active = banking_data[:,4].astype(float)
to_months = years_active * 12

print(f"Years active to months: \n{to_months}")

# output:

# Years active to months: 
# [ 72.  84.  36.  60.  48.  48.  72. 120. 144.  24.]


# **Q14.2:** Calculate the average years active

years_active = banking_data[:,4].astype(float)
avg_years = np.mean(years_active)

print(f"Average years active: {avg_years}")

# output:

# Average years active: 5.9


# **Q14.3:** Find customers who have been active for more than 5 years

years_active = banking_data[:,4].astype(float)
customer_id = banking_data[:,0]
customer_grater_5 = customer_id[years_active > 5]

print(f"Customers who have been active for more than 5 years: \n{customer_grater_5}")

# output:

# Customers who have been active for more than 5 years: 
# ['C999' 'C623' 'C205' 'C412' 'C856']


# **Q14.4:** Calculate the total time all customers have been active (in years)

years_active = banking_data[:,4].astype(float)
total_time = np.sum(years_active)

print(f"Total time all customers have been active (in years): {total_time}")

# output:

# Total time all customers have been active (in years): 59.0


# **Q14.5:** Find the customer with the shortest time active

years_active = banking_data[:,4].astype(float)
min_index = np.argmin(years_active)
customer_id = banking_data[:,0]
min_active_customer = customer_id[min_index]

print(f"Customer with the shortest time active: {min_active_customer}")

# output:

# Customer with the shortest time active: C309