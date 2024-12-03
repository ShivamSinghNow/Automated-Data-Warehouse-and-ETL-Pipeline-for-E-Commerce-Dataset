USE ecommerce; 

CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id INT PRIMARY KEY, 
    name VARCHAR(255), 
    email VARCHAR(255), 
    address VARCHAR(255)
); 

CREATE TABLE IF NOT EXISTS fact_sales (
    order_id INT PRIMARY KEY, 
    product_id INT, 
    customer_id INT, 
    quantity INT, 
    total_amount DECIMAL(10,2), 
    order_date DATE, 
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id)
); 

INSERT INTO dim_customers (customer_id, name, email, address)
SELECT customer_id, name, email, address FROM customers; 

INSERT INTO fact_sales(order_id, product_id, customer_id, quantity, total_amount, order_date)
SELECT order_id, product_id, customer_id, quantity, quantity * price AS total_amount, order_date
FROM sales; 