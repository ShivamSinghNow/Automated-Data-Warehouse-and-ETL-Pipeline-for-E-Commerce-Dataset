USE ecommerce;

SELECT 
    MONTH(order_date) AS order_month, 
    SUM(total_amount) AS total_amount

FROM fact_sales
GROUP BY order_month
ORDER BY order_month


SELECT
    customer_id, 
    SUM(total_amount) AS total_spending

FROM fact_sales
GROUP BY customer_id
ORDER BY total_spending DESC
LIMIT 5; 

