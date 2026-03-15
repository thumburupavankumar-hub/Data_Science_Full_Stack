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

-- # DATE FUNCTIONS – 20 Questions

-- 1. Extract year from Order_Date.

SELECT EXTRACT(YEAR FROM Order_Date) AS Order_Year
FROM ORDERS;

-- 2. Extract month from Order_Date.

SELECT EXTRACT(MONTH FROM Order_Date) AS ORDER_MONTH
FROM ORDERS;

-- 3. Extract day from Order_Date.

SELECT EXTRACT(DAY FROM Order_Date) AS ORDER_DAY
FROM ORDERS;

-- 4. Find current date.

SELECT SYSDATE AS SYS_DATE
FROM DUAL;

-- 5. Find current timestamp.

SELECT SYSTIMESTAMP AS TIME_STAMP
FROM DUAL;

-- 6. Add 7 days to Order_Date.

SELECT ORDER_DATE, Order_Date + 7
FROM ORDERS;

-- 7. Subtract 30 days from Order_Date.

SELECT ORDER_DATE, Order_Date - 30
FROM ORDERS;

-- 8. Find difference between two dates.

SELECT SYSDATE - ORDER_DATE AS DATE_DIFFERENCE
FROM ORDERS;

-- 9. Find number of months between two dates.

SELECT
    ORDER_DATE,
    SYSDATE,
    EXTRACT(MONTH FROM ORDER_DATE) - EXTRACT(MONTH FROM SYSDATE) AS MONTH_DIFFERENCE
FROM ORDERS;

-- 10. Find last day of the month.

SELECT LAST_DAY(ORDER_DATE) AS LAST_DAY_OF_MONTH
FROM ORDERS;

-- 11. Get first day of the year.

SELECT TRUNC(ORDER_DATE,'YYYY') AS FIRST_DAY_OF_YEAR
FROM ORDERS;

-- 12. Format date as 'DD-MM-YYYY'.

SELECT TO_CHAR(ORDER_DATE,'DD-MM-YYYY') AS NEW_FORMAT
FROM ORDERS;

-- 13. Convert string to date.

SELECT TO_DATE(ORDER_DATE, 'DD-MM-YYYY')
FROM ORDERS;

-- 14. Convert date to string.

SELECT TO_CHAR(ORDER_DATE,'DD-MM-YYYY')
FROM ORDERS;

-- 15. Find week number of the year.

SELECT TO_CHAR(ORDER_DATE,'WW') AS WEEK_NUMBER
FROM ORDERS;

-- 16. Find day name from date.

SELECT TO_CHAR(ORDER_DATE,'DAY') AS DAY_NAME
FROM ORDERS;

-- 17. Find quarter of the year.

SELECT TO_CHAR(ORDER_DATE,'Q') AS QUARTER_YEAR
FROM ORDERS;

-- 18. Calculate age from DOB.

SELECT FLOOR(MONTHS_BETWEEN(SYSDATE, ORDER_DATE) / 12) AS AGE
FROM ORDERS;

-- 19. Check if date is weekend.

SELECT ORDER_DATE,
    CASE
        WHEN TRIM(TO_CHAR(ORDER_DATE,'DAY')) IN ('SATURDAY','SUNDAY')
        THEN 'WEEKEND'
        ELSE 'WEEKDAY'
    END AS DAY_TYPE
FROM ORDERS;

-- 20. Find next Monday after a given date.

SELECT NEXT_DAY(ORDER_DATE,'MONDAY') AS NEXT_MONDAY
FROM ORDERS;