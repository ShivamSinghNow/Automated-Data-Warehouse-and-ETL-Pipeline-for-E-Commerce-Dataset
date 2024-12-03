import pandas as pd 
import random 
import json 
from faker import Faker

fake = Faker()

NUM_CUST = 1000 
NUM_SALES = 1000 

def generate_customers(num_customers): 
    customers = []
    for cust_id in range(1, num_customers + 1): 
        customers.append({
            "customer_id" : cust_id, 
            "name" : fake.name(),
            "email" : fake.email(), 
            "address" : fake.address().replace("\n", ", "),
        })
    return customers

def generate_sales(num_sales, num_customers): 
    sales = []
    for order_id in range(1, num_sales + 1): 
        sales.append({
            "order_id" : order_id, 
            "product_id" : random.randint(100, 500), 
            "customer_id" : random.randint(1, num_customers), 
            "quantity" : random.randint(1, 5), 
            "price": round(random.uniform(5, 100), 2), 
            "order_date" : fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
        })
    
    return sales

def save_data(): 
    customers = generate_customers(NUM_CUST)
    sales = generate_sales(NUM_SALES, NUM_CUST)

    with open("customers_data.json", "w") as f: 
        json.dump(customers, f, indent = 4)

    sales_df = pd.DataFrame(sales)
    sales_df.to_csv("sales_data.csv", index = False)
    print("Dataset has successfully been generated")


if __name__ == "__main__": 
    save_data()
