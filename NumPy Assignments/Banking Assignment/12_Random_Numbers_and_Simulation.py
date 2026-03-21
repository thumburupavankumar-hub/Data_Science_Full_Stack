# ### Question 11: Random Numbers and Simulation


# **Q11.1:** Generate 6 random integers between 1 and 1000

random_int = np.random.randint(1,1000,6)

print(f"6 random integers between 1 and 1000: \n{random_int}")

# output:

# 6 random integers between 1 and 1000: 
# [ 35 203 584 390 931 925]


# **Q11.2:** Generate 6 random floats between 0 and 1

random_float = np.random.random(6)

print(f"6 random floats between 0 and 1: \n{random_float}")

# output:

# 6 random floats between 0 and 1: 
# [0.66821394 0.21527097 0.06889615 0.14691607 0.05578326 0.42337948]


# **Q11.3:** Generate 6 random numbers from normal distribution (mean=700, std=100)

rand_noramal_distribution = np.random.normal(loc=700, scale=100, size=6)

print(f"6 random numbers from normal distribution (mean=700, std=100): \n{rand_noramal_distribution}")

# output:

# 6 random numbers from normal distribution (mean=700, std=100): 
# [633.04201807 761.88873557 812.51109139 863.88345812 637.55640731
#  800.73564683]


# **Q11.4:** Shuffle the `banking_data` rows randomly

np.random.shuffle(banking_data)

print(f"Shuffled the `banking_data` rows randomly: \n{banking_data}")

# output:

# Shuffled the `banking_data` rows randomly: 
# [['C623' '9800' '710' '18' '7']
#  ['C205' '8900' '680' '20' '6']
#  ['C999' '7200' '705' '16' '6']
#  ['C912' '3500' '660' '11' '5']
#  ['C101' '5200' '720' '15' '4']
#  ['C309' '1200' '610' '8' '2']
#  ['C856' '11200' '770' '30' '12']
#  ['C412' '15000' '750' '25' '10']
#  ['C587' '4300' '690' '12' '3']
#  ['C744' '2750' '640' '9' '4']]


# **Q11.5:** Set random seed to 123 and generate 4 random numbers

set_rand_seed = np.random.seed(123)
rand_seed = np.random.rand(4)

print(f"Random seed to 123, 4 random numbers: \n{rand_seed}")

# output:

# Random seed to 123, 4 random numbers: 
# [0.69646919 0.28613933 0.22685145 0.55131477]