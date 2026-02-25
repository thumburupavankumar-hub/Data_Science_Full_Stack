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
    INTO Orders VALUES (1005, TO_DATE('2026-02-05','YYYY-MM-DD'), 'C005', 'Kiran Rao', 'Home Kitchen', 'Mixer Grinder', 1, 2499, 'UPI', 'Bangalore')
    INTO Orders VALUES (1006, TO_DATE('2026-02-06','YYYY-MM-DD'), 'C006', 'Neha Verma', 'Beauty', 'Face Cream', 4, 299, 'Credit Card', 'Delhi')
    INTO Orders VALUES (1007, TO_DATE('2026-02-07','YYYY-MM-DD'), 'C007', 'Rahul Das', 'Grocery', 'Cooking Oil 1L', 5, 180, 'Cash', 'Kolkata')
    INTO Orders VALUES (1008, TO_DATE('2026-02-08','YYYY-MM-DD'), 'C008', 'Anjali Nair', 'Fashion', 'Women''s Jeans', 2, 1199, 'UPI', 'Kochi')
    INTO Orders VALUES (1009, TO_DATE('2026-02-09','YYYY-MM-DD'), 'C009', 'Suresh Patel', 'Electronics', 'Smartphone', 1, 15999, 'Debit Card', 'Ahmedabad')
    INTO Orders VALUES (1010, TO_DATE('2026-02-10','YYYY-MM-DD'), 'C010', 'Meena Iyer', 'Home Kitchen', 'Pressure Cooker', 1, 1899, 'Credit Card', 'Pune');

-- # NUMERICAL FUNCTIONS – 20 Questions


-- 1. Round Unit_Price to 2 decimal places.

SELECT ROUND(Unit_Price, 2)
FROM Orders;

-- 2. Find total sales per order.

SELECT Order_ID,
       Quantity * Unit_Price AS Total_Sales
FROM Orders;

-- 3. Calculate average order value.

SELECT Order_ID,
       AVG(Quantity * Unit_Price) AS AVG_VALUE
FROM Orders
GROUP BY Order_ID;

-- 4. Find highest product price.

SELECT MAX(Unit_Price)
FROM ORDERS;

-- 5. Find lowest product price.

SELECT MIN(Unit_Price)
FROM ORDERS;

-- 6. Calculate percentage discount applied.

SELECT Unit_Price,
    Unit_Price * 0.10 AS Discount,
    (0.10 * 100) AS Discount_Percentage
FROM Orders;

-- 7. Find modulus of Quantity divided by 2.

SELECT MOD(Quantity,2)
FROM Orders;

-- 8. Convert negative values to positive.

SELECT ABS(Unit_Price)
FROM ORDERS;

-- 9. Truncate price without rounding.

SELECT TRUNC(Unit_Price,0)
FROM ORDERS;

-- 10. Find square root of total sales.

SELECT SQRT(QUANTITY * UNIT_PRICE)
FROM ORDERS;

-- 11. Calculate exponential value of a number.

SELECT EXP(2)
FROM DUAL;

-- 12. Calculate power of 2^5.

SELECT POWER(2,5)
FROM DUAL;

-- 13. Find absolute difference between two prices.

SELECT ABS(MAX(UNIT_PRICE)-MIN(UNIT_PRICE))
FROM ORDERS;

-- 14. Calculate sales growth percentage.

SELECT ((2000-1500)/1500)*100
FROM DUAL;

-- 15. Find random number between 1 and 100.

SELECT TRUNC(DBMS_RANDOM.VALUE(1,101))
FROM DUAL;

-- 16. Divide total sales by number of orders.

SELECT SUM(Quantity * Unit_Price) / COUNT(*)
FROM Orders;

-- 17. Find ceiling value of price.

SELECT CEIL(UNIT_PRICE)
FROM ORDERS;

-- 18. Find floor value of price.

SELECT FLOOR(UNIT_PRICE)
FROM ORDERS;

-- 19. Convert decimal to integer.

SELECT TRUNC(Unit_Price)
FROM Orders;

-- 20. Calculate compound interest.

SELECT 10000 * POWER((1+0.05),2)
FROM DUAL;