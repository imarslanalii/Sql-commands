# CREATE DATABASE test;
# DROP DATABASE test;

# CREATE TABLE customers(
# 	id INT NOT NULL AUTO_INCREMENT,
# 	field1 VARCHAR(255),
# 	field2 VARCHAR(255),
# 	field3 VARCHAR(255),
# 	PRIMARY KEY(id)
# );

# INSERT INTO customers (field1, field2, field3) 
# VALUES (‘value1A’, ‘value2A’, ‘value3A’), 
# (‘value1B’, ‘value2B’, ‘value3B’), 
# (‘value1C’, ‘value2C’, ‘value3C’);

# UPDATE customers
# SET email = 'test@gmail.com'
# WHERE id = 3;

# DELETE FROM customers
# Where id = 3;

# ALTER TABLE customers ADD testCol VARCHAR(255);

# ALTER TABLE customers
# MODIFY COLUMN testCol int(11);       // could be ALTER COLUMN in other DBMS

# ALTER TABLE customers
# DROP COLUMN testCol;

# SELECT 

# SELECT *(staric use for all) FROM customers;
# SELECT field1, field2 FROM customers;
# SELECT * FROM customers WHERE id = 3;
# SELECT * FROM customers ORDER BY field2;
# SELECT * FROM customers ORDER BY field2 DESC(descending);
# SELECT DISTINCT field2 FROM customers;
# SELECT * FROM customers WHERE age < 30;

# SQL OPERATOR

# SELECT * FROM customers
# WHERE age
# BETWEEN 22 AND 30;

# SELECT * FROM customers
# WHERE field2 LIKE ‘%n’(if word end with n); 

# SELECT * FROM customers
# WHERE field2 LIKE ‘%n%’(if any leters have n); 

# SELECT * FROM customers
# WHERE field2 NOT LIKE ‘%n%’(don't have n); 

# SELECT * FROM customers
# WHERE field2 IN (‘query1’, ‘query2’);

# INDEXES (to find data mpre quickly)

# CREATE INDEX CIndex
# ON customers(field1);
# DROP INDEX CIndex ON customers;

# CREATE TABLE products (
# 	id INT NOT NULL AUTO_INCREMENT,
# 	name VARCHAR(255),
# 	price INT,
# 	PRIMARY KEY(id)
# );

# CREATE TABLE orders (
# 	id INT NOT NULL AUTO_INCREMENT,
# 	orderNumber INT,
# 	productId INT,
# 	customerId INT,
#   age int,
# 	orderDate DATETIME default CURRENT_TIMESTAMP,
# 	PRIMARY KEY(id),
#       FOREIGN KEY(customerId) REFERENCES customers(id),
#       FOREIGN KEY(productId) REFERENCES products(id)
# );

# JOINS (used to combine rows based on a comman field btw them)

# SELECT customers.field1, customers.field2, orders.orderNumber
# FROM customers
# INNER JOIN orders
# ON customers.id = orders.customerId
# ORDER BY orders.orderNumber;

# SELECT customers.field1, customers.field2, orders.orderNumber, orders.orderDate
# FROM customers
# LEFT JOIN orders
# ON customers.id = orders.customerId
# ORDER BY customers.field2;

# SELECT orders.orderNumber, customers.field1, customers.field2
# FROM orders
# RIGHT JOIN customers
# ON orders.customerId = customers.id
# ORDER BY orders.orderNumber;

# SELECT orders.orderNumber customers.field1 customers.field2 products.name
# FROM orders
# INNER JOIN products
# ON orders.productId = products.id
# INNER JOIN customers
# ON orders.customerId = customers.id
# ORDER BY orders.orderNumber;

# ALIASES (give temporary name of columns and rows)

# SELECT field1 AS ‘First Name’, field2 AS ‘Last Name’ FROM customers;
# SELECT CONCAT(field1,' ', field2) AS ‘Name’, field3, FROM customers; 
# SELECT o.id, o.orderDate, c.field1, c.field2
# FROM customers AS c, orders AS o;

# SQL Aggregate Functions

# SELECT AVG(age) FROM customers;
# SELECT COUNT(field3) FROM customers;
# SELECT MAX(field3) FROM customers;
# SELECT MIN(field3) FROM customers;
# SELECT SUM(field3) FROM customers;

# SELECT field3, COUNT(field3) 
# FROM customers
# WHERE field3 > 30
# GROUP BY field3;

# SELECT field3, COUNT(field3) 
# FROM customers
# GROUP BY field3
# HAVING COUNT(field3) >= 2;

# SELECT UCASE(field1) FROM customers;
# SELECT LCASE(field1) FROM customers;
