
-- # MATHEMATIC FUNCTIONS – 20 Questions

-- 1. Find sine value of an angle.

SELECT CEIL(SIN(90)) AS SIN_VALUE
FROM DUAL;

-- 2. Find cosine value of an angle.

SELECT ROUND(COS(90),2) AS COS_VALUE
FROM DUAL;

-- 3. Find tangent value.

SELECT ROUND(TAN(90),2) AS TAN_VALUE
FROM DUAL;

-- 4. Convert degrees to radians.

SELECT ROUND(30 * (ACOS(-1) / 180),2) AS radians
FROM dual;

-- 5. Convert radians to degrees.

SELECT ROUND(5 * (180 / ACOS(-1)),2) AS degrees
FROM dual;

-- 6. Find logarithm (base 10) of a number.

SELECT LOG(10, 100) AS LOG_BASE_10
FROM DUAL;

-- 7. Find natural log of a number.

SELECT LN(10) AS NATURAL_LOG
FROM DUAL;

-- 8. Find square of a number.

SELECT POWER(4,2) AS SQUARE
FROM DUAL;

-- 9. Find cube of a number.

SELECT POWER(4,3) AS CUBE
FROM DUAL;

-- 10. Calculate factorial of a number.

SELECT 5,
       PRODUCT
FROM (
    SELECT EXP(SUM(LN(LEVEL))) AS PRODUCT
    FROM dual
    CONNECT BY LEVEL <= 5
);

-- 11. Find greatest value among three numbers.

SELECT GREATEST(10, 20, 15) AS GREATEST_VALUE
FROM dual;

-- 12. Find least value among three numbers.

SELECT LEAST(10, 20, 15) AS LEAST_VALUE
FROM dual;

-- 13. Calculate variance of sales.

SELECT VARIANCE(Unit_Price * Quantity) AS VARIANCE_SALES
FROM ORDERS;

-- 14. Calculate standard deviation of sales.

SELECT STDDEV(QUANTITY*UNIT_PRICE) AS stddev_sales
FROM ORDERS;

-- 15. Find average deviation.

SELECT AVG(ABS(UNIT_PRICE - avg_val)) AS avg_deviation
FROM (
    SELECT UNIT_PRICE,
           AVG(UNIT_PRICE) OVER () AS avg_val
    FROM ORDERS
);

-- 16. Calculate geometric mean.

SELECT EXP(AVG(LN(UNIT_PRICE))) AS geometric_mean
FROM ORDERS
WHERE UNIT_PRICE > 0;

-- 17. Calculate harmonic mean.

SELECT COUNT(UNIT_PRICE) / SUM(1/UNIT_PRICE) AS harmonic_mean
FROM ORDERS
WHERE UNIT_PRICE <> 0;

-- 18. Find sum of squares.

SELECT SUM(POWER(UNIT_PRICE, 2)) AS sum_of_squares
FROM ORDERS;

-- 19. Calculate correlation between two columns.

SELECT CORR(UNIT_PRICE, QUANTITY) AS correlation
FROM ORDERS;

-- 20. Calculate regression slope.

SELECT REGR_SLOPE(QUANTITY, UNIT_PRICE) AS regression_slope
FROM ORDERS;