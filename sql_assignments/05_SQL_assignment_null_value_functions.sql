-- # NULL VALUE FUNCTIONS – 20 Questions

-- 1. Replace NULL price with 0.

SELECT COALESCE(UNIT_PRICE, 0)
FROM ORDERS;

-- 2. Replace NULL Customer_Name with 'Unknown'.

SELECT COALESCE(CUSTOMER_NAME,'UNKNOWN')
FROM ORDERS;

-- 3. Count NULL values in Product_Name.

SELECT COUNT(*) AS NULL_PRODUCT_NAME
FROM ORDERS
WHERE PRODUCT_NAME IS NULL;

-- 4. Find rows where Order_Date is NULL.

SELECT ORDER_ID
FROM ORDERS
WHERE ORDER_DATE IS NULL;

-- 5. Use COALESCE to return first non-null value.

SELECT COALESCE(NULL, NULL, 'Oracle', 'SQL') AS result
FROM dual;

-- 6. Use NVL to replace NULL values.

SELECT NVL(NULL, 'Oracle')
FROM DUAL;

-- 7. Use IFNULL function.

SELECT IFNULL(NULL, 'Oracle')
FROM DUAL;

-- 8. Check if column is NULL.

SELECT *
FROM ORDERS
WHERE PRODUCT_NAME IS NULL;

-- 9. Check if column is NOT NULL.

SELECT *
FROM ORDERS
WHERE PRODUCT_NAME IS NOT NULL;

-- 10. Use NULLIF between two columns.

SELECT NULLIF(Product_Category, Product_Name) 
FROM ORDERS;

-- 11. Replace blank values with NULL.

SELECT
    CASE
        WHEN TRIM(PRODUCT_NAME)IS NULL THEN ''
        ELSE PRODUCT_NAME
    END
FROM ORDERS;

-- 12. Count non-null values.

SELECT COUNT(*) AS NON_NULL
FROM ORDERS
WHERE PRODUCT_NAME IS NOT NULL;

-- 13. Filter records where price is NULL or 0.

SELECT *
FROM ORDERS
WHERE UNIT_PRICE IS NULL
    OR UNIT_PRICE = 0;

-- 14. Use CASE to handle NULL values.

SELECT
    CASE
        WHEN UNIT_PRICE IS NULL THEN 0
        ELSE UNIT_PRICE
    END AS UNIT_PRICE
FROM ORDERS;

-- 15. Compare NULL values properly.

SELECT PRODUCT_NAME, PRODUCT_CATEGORY
FROM ORDERS
WHERE PRODUCT_NAME IS NULL AND PRODUCT_CATEGORY IS NULL;

-- 16. Handle NULL in aggregation.

SELECT COUNT(NULL) AS NULL_VALUES
FROM ORDERS;

-- 17. Find average excluding NULL values.

SELECT AVG(UNIT_PRICE) AS AVG_UNIT_PRICE
FROM ORDERS;

-- 18. Find sum ignoring NULL values.

SELECT SUM(UNIT_PRICE)
FROM ORDERS
WHERE UNIT_PRICE IS NOT NULL;

-- 19. Identify columns containing NULL using metadata.

SELECT *
FROM ORDERS
WHERE ORDER_ID IS NULL
   OR PRODUCT_NAME IS NULL
   OR UNIT_PRICE IS NULL
   OR ORDER_DATE IS NULL;

-- 20. Convert NULL to default system date.

SELECT NVL(order_date, SYSDATE) AS order_date
FROM ORDERS;