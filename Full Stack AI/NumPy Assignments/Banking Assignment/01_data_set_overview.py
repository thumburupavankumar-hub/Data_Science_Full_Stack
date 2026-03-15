# # NumPy Assignment: Banking Industry Analysis - Questions Only

# ## Dataset Overview
# The assignment uses banking industry data with 10 rows × 5 columns:
# - **Customer_ID**: Unique identifier for each customer
# - **Account_Balance**: Customer's account balance in dollars
# - **Credit_Score**: Customer's credit score (300-900 range)
# - **Transaction_Count**: Number of transactions in the last month
# - **Years_Active**: Number of years the customer has been with the bank

import numpy as np
import pandas as pd

banking_data = np.array([
    ['C101', 5200, 720, 15, 4],
    ['C205', 8900, 680, 20, 6],
    ['C309', 1200, 610, 8, 2],
    ['C412', 15000, 750, 25, 10],
    ['C587', 4300, 690, 12, 3],
    ['C623', 9800, 710, 18, 7],
    ['C744', 2750, 640, 9, 4],
    ['C856', 11200, 770, 30, 12],
    ['C912', 3500, 660, 11, 5],
    ['C999', 7200, 705, 16, 6]
])

print(banking_data)

# output:

"""
[['C101' '5200' '720' '15' '4']
 ['C205' '8900' '680' '20' '6']
 ['C309' '1200' '610' '8' '2']
 ['C412' '15000' '750' '25' '10']
 ['C587' '4300' '690' '12' '3']
 ['C623' '9800' '710' '18' '7']
 ['C744' '2750' '640' '9' '4']
 ['C856' '11200' '770' '30' '12']
 ['C912' '3500' '660' '11' '5']
 ['C999' '7200' '705' '16' '6']]
 """