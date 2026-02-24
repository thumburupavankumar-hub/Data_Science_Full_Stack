-- Create Table
CREATE TABLE Orders (
    Order_ID NUMBER PRIMARY KEY,
    Order_Date DATE,
    Customer_ID VARCHAR2(10),
    Customer_Name VARCHAR2(100),
    Product_Category VARCHAR2(100),
    Product_Name VARCHAR2(150),
    Quantity NUMBER,
    Unit_Price NUMBER(10,2),
    Payment_Mode VARCHAR2(50),
    Store_Location VARCHAR2(100)
);

-- Insert Data
INSERT ALL
    INTO Orders VALUES (1001, TO_DATE('2026-02-01','YYYY-MM-DD'), 'C001', 'Ravi Kumar', 'Electronics', 'Wireless Mouse', 2, 799, 'UPI', 'Bangalore')
    INTO Orders VALUES (1002, TO_DATE('2026-02-02','YYYY-MM-DD'), 'C002', 'Sneha Reddy', 'Grocery', 'Basmati Rice 5kg', 1, 650, 'Credit Card', 'Hyderabad')
    INTO Orders VALUES (1003, TO_DATE('2026-02-03','YYYY-MM-DD'), 'C003', 'Arjun Mehta', 'Fashion', 'Men''s T-Shirt', 3, 499, 'Cash', 'Chennai')
    INTO Orders VALUES (1004, TO_DATE('2026-02-04','YYYY-MM-DD'), 'C004', 'Priya Sharma', 'Electronics', 'Bluetooth Speaker', 1, 1499, 'Debit Card', 'Mumbai')
    INTO Orders VALUES (1005, TO_DATE('2026-02-05','YYYY-MM-DD'), 'C005', 'Kiran Rao', 'Home & Kitchen', 'Mixer Grinder', 1, 2499, 'UPI', 'Bangalore')
    INTO Orders VALUES (1006, TO_DATE('2026-02-06','YYYY-MM-DD'), 'C006', 'Neha Verma', 'Beauty', 'Face Cream', 4, 299, 'Credit Card', 'Delhi')
    INTO Orders VALUES (1007, TO_DATE('2026-02-07','YYYY-MM-DD'), 'C007', 'Rahul Das', 'Grocery', 'Cooking Oil 1L', 5, 180, 'Cash', 'Kolkata')
    INTO Orders VALUES (1008, TO_DATE('2026-02-08','YYYY-MM-DD'), 'C008', 'Anjali Nair', 'Fashion', 'Women''s Jeans', 2, 1199, 'UPI', 'Kochi')
    INTO Orders VALUES (1009, TO_DATE('2026-02-09','YYYY-MM-DD'), 'C009', 'Suresh Patel', 'Electronics', 'Smartphone', 1, 15999, 'Debit Card', 'Ahmedabad')
    INTO Orders VALUES (1010, TO_DATE('2026-02-10','YYYY-MM-DD'), 'C010', 'Meena Iyer', 'Home & Kitchen', 'Pressure Cooker', 1, 1899, 'Credit Card', 'Pune');

-- # STRING FUNCTIONS – 20 Questions


-- 1. Write a query to convert all customer names to uppercase.

SELECT 
UPPER(Customer_Name)
FROM Orders;

-- 2. Extract the first 5 characters from Product_Name.

SELECT SUBSTR(Product_Name,1,5) AS First_five
FROM Orders;

-- 3. Find the length of each Customer_Name.

SELECT LENGTH(Customer_Name) AS Name_Length
FROM Orders;

-- 4. Replace the word "Rice" with "Premium Rice" in Product_Name.

SELECT REPLACE(Product_Name,'Rice','Premium Rice') 
FROM Orders;

-- 5. Remove leading and trailing spaces from Customer_Name.

SELECT TRIM(Customer_Name)
FROM Orders;

-- 6. Concatenate First_Name and Last_Name as Full_Name.

SELECT
Customer_Name || ' ' || Product_Name AS Customer_Product
FROM Orders; -- Here First_Name and Last_Name is not exists. So I'm using Customer_Name and Product_Name AS Customer_Product

-- 7. Find customers whose names start with 'A'.

SELECT Customer_Name
FROM Orders
WHERE Customer_Name LIKE 'A%'

-- 8. Extract the domain name from Email_ID.

SELECT SUBSTR(Email_ID,
              INSTR(Email_ID,'@')+1)
FROM Orders;

-- 9. Find the position of '@' in Email_ID.

SELECT INSTR(Email_ID,'@') AS Position_Of_At
FROM Orders;

-- 10. Reverse the Product_Name.

SELECT REVERSE(Product_Name) AS REVERSE_NAME
FROM Orders;

-- 11. Convert the first letter of each word in Product_Name to uppercase.

SELECT INITCAP(Product_Name)
FROM Orders;

-- 12. Extract the last 3 characters from Order_ID.

SELECT SUBSTR(Order_ID,-3) AS LAST_THREE
FROM ORDERS;

-- 13. Count how many times letter 'a' appears in Customer_Name.

SELECT 
Customer_Name,
LENGTH(Customer_Name) - LENGTH(REPLACE(LOWER(Customer_Name),'a','')) AS A_Count
FROM Orders;

-- 14. Mask the last 4 digits of a phone number.

SELECT 
SUBSTR(Phone_Number,1,LENGTH(Phone_Number)-4) || '****' AS Masked_Number
FROM Orders;

-- 15. Split Full_Name into First_Name and Last_Name.

SELECT
SUBSTR(Full_Name,1,INSTR(Full_Name,' ')-1) AS First_Name,
SUBSTR(Full_Name,INSTR(Full_Name,' ')+1) AS Last_Name
FROM Orders;

-- 16. Remove all special characters from Product_Code.

SELECT 
REGEXP_REPLACE(Product_Code, '[^A-Za-z0-9]', '') AS Clean_Product_Code
FROM Orders;

-- 17. Compare two columns ignoring case sensitivity.

SELECT *
FROM Orders
WHERE LOWER(Product_Name) = LOWER(Product_Category);

-- 18. Find customers whose name contains 'kumar'.

SELECT Customer_Name
FROM Orders
WHERE LOWER(Customer_Name) LIKE '%kumar%';

-- 19. Pad Order_ID with leading zeros to make it 6 digits.

SELECT 
LPAD(Order_ID,6,'0') AS Padded_Order_ID
FROM Orders;

-- 20. Extract substring between two characters.

SELECT 
SUBSTR(Product_Name,
       INSTR(Product_Name,'(')+1,
       INSTR(Product_Name,')') - INSTR(Product_Name,'(') - 1) AS Extracted_Text
FROM Orders;