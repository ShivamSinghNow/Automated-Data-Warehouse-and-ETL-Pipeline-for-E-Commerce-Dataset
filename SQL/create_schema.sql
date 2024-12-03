CREATE DATABASE IF NOT EXISTS ecommerce; 

USE ecommerce; 

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY, 
    name VARCHAR(255), 
    email VARCHAR(255), 
    address VARCHAR(255)
); 


CREATE TABLE IF NOT EXISTS sales(
    order_id INT PRIMARY KEY, 
    product_id INT, 
    customer_id INT, 
    quantity INT, 
    price DECIMAL(10,2), 
    order_date DATE, 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
); 
