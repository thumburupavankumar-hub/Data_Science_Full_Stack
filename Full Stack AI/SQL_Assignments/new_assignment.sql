CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT
);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 70000),
(2, 'Mouse', 'Electronics', 500),
(3, 'Keyboard', 'Electronics', 1500),
(4, 'Office Chair', 'Furniture', 8000),
(5, 'Desk', 'Furniture', 12000);


CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT,
    warehouse VARCHAR(50),
    stock_quantity INT
);

INSERT INTO inventory VALUES
(101, 1, 'Warehouse_A', 50),
(102, 1, 'Warehouse_B', 30),
(103, 2, 'Warehouse_A', 200),
(104, 3, 'Warehouse_A', 150),
(105, 6, 'Warehouse_B', 40);


SELECT 
p.product_name,
i.warehouse,
i.stock_quantity
FROM products p
INNER JOIN inventory i
ON p.product_id = i.product_id;




SELECT 
p.product_name,
i.warehouse,
i.stock_quantity
FROM products p
LEFT JOIN inventory i
ON p.product_id = i.product_id;




SELECT 
p.product_name,
i.warehouse,
i.stock_quantity
FROM products p
RIGHT JOIN inventory i
ON p.product_id = i.product_id;


SELECT 
p.product_name,
i.warehouse,
i.stock_quantity
FROM products p
FULL OUTER JOIN inventory i
ON p.product_id = i.product_id;



SELECT 
p.product_name,
i.warehouse
FROM products p
CROSS JOIN inventory i;





-- ================================
-- Inventory JOIN Practice Questions & Answers
-- Tables Used:
-- products(product_id, product_name, category, price)
-- inventory(inventory_id, product_id, warehouse, stock_quantity)
-- ================================


-- 1. Show all products with their warehouse and stock quantity.
SELECT p.product_name, i.warehouse, i.stock_quantity
FROM products p
JOIN inventory i
ON p.product_id = i.product_id;


-- 2. Show all products even if they do not exist in inventory.
SELECT p.product_name, i.warehouse, i.stock_quantity
FROM products p
LEFT JOIN inventory i
ON p.product_id = i.product_id;


-- 3. Show all inventory records even if product details are missing.
SELECT p.product_name, i.warehouse, i.stock_quantity
FROM products p
RIGHT JOIN inventory i
ON p.product_id = i.product_id;


-- 4. Show all records from both tables (matched and unmatched).
SELECT p.product_name, i.warehouse, i.stock_quantity
FROM products p
FULL OUTER JOIN inventory i
ON p.product_id = i.product_id;


-- 5. Find products available in Warehouse_A.
SELECT p.product_name, i.stock_quantity
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
WHERE i.warehouse = 'Warehouse_A';


-- 6. Find products available in Warehouse_B.
SELECT p.product_name, i.stock_quantity
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
WHERE i.warehouse = 'Warehouse_B';


-- 7. Find products with stock greater than 100.
SELECT p.product_name, i.stock_quantity
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
WHERE i.stock_quantity > 100;


-- 8. Find total stock for each product.
SELECT p.product_name, SUM(i.stock_quantity) AS total_stock
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
GROUP BY p.product_name;


-- 9. Find the total inventory value for each product.
SELECT p.product_name,
SUM(p.price * i.stock_quantity) AS inventory_value
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
GROUP BY p.product_name;


-- 10. Find products that do not exist in inventory.
SELECT p.product_name
FROM products p
LEFT JOIN inventory i
ON p.product_id = i.product_id
WHERE i.product_id IS NULL;


-- 11. Find inventory records with no matching product.
SELECT i.inventory_id, i.product_id
FROM inventory i
LEFT JOIN products p
ON p.product_id = i.product_id
WHERE p.product_id IS NULL;


-- 12. Find product names and categories stored in Warehouse_A.
SELECT p.product_name, p.category, i.warehouse
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
WHERE i.warehouse = 'Warehouse_A';


-- 13. Find the number of warehouses storing each product.
SELECT p.product_name, COUNT(i.warehouse) AS warehouse_count
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
GROUP BY p.product_name;


-- 14. Find the highest stock quantity for each product.
SELECT p.product_name, MAX(i.stock_quantity) AS highest_stock
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
GROUP BY p.product_name;


-- 15. Find the lowest stock quantity for each product.
SELECT p.product_name, MIN(i.stock_quantity) AS lowest_stock
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
GROUP BY p.product_name;


-- 16. Find products and their price along with stock quantity.
SELECT p.product_name, p.price, i.stock_quantity
FROM products p
JOIN inventory i
ON p.product_id = i.product_id;


-- 17. Find total stock available in each warehouse.
SELECT i.warehouse, SUM(i.stock_quantity) AS total_stock
FROM inventory i
GROUP BY i.warehouse;


-- 18. Find products whose total stock is greater than 200.
SELECT p.product_name, SUM(i.stock_quantity) AS total_stock
FROM products p
JOIN inventory i
ON p.product_id = i.product_id
GROUP BY p.product_name
HAVING SUM(i.stock_quantity) > 200;


-- 19. Find all combinations of products and warehouses.
SELECT p.product_name, i.warehouse
FROM products p
CROSS JOIN inventory i;


-- 20. Find products that exist in both tables (semi join concept).
SELECT DISTINCT p.product_name
FROM products p
JOIN inventory i
ON p.product_id = i.product_id;