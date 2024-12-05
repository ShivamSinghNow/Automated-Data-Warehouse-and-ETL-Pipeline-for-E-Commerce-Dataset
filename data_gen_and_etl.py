import pandas as pd
import random
import json
from faker import Faker
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError

fake = Faker()
fake_unique = fake.unique

# Define the number of new records to generate daily
NUM_NEW_CUSTOMERS = 10000  # Generate 10,000 new customers each run
NUM_NEW_SALES = 50000      # Generate 50,000 new sales each run

# Define AWS RDS MySQL connection details
aws_rds_endpoint = 'my-ecommerce-db.cn68aoymgc0l.us-west-1.rds.amazonaws.com'  # Replace with your AWS RDS endpoint
db_user = 'shiv'  # Replace with your database username
db_password = 'Awesomeward15$'  # Replace with your password
db_name = 'ecommerce'

# Update the MySQL connection string
engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{aws_rds_endpoint}:3306/{db_name}', pool_size=10, max_overflow=20)

# Generate new customer data with unique email addresses
def generate_customers(num_customers, start_id):
    customers = []

    # Fetch all existing emails from the database to ensure uniqueness
    with engine.connect() as conn:
        try:
            result = conn.execute(text("SELECT email FROM customers"))
            existing_emails = {row[0] for row in result.fetchall()}
        except Exception as e:
            print(f"Error fetching existing emails from database: {e}")
            existing_emails = set()

    used_emails = existing_emails

    for cust_id in range(start_id, start_id + num_customers):
        email = fake.email()
        # Ensure unique email manually if it already exists in the used_emails set
        while email in used_emails:
            email = fake.email()
        used_emails.add(email)

        customers.append({
            "customer_id": cust_id,
            "name": fake.name(),
            "email": email,  # Ensure the email is unique
            "address": fake.address().replace("\n", ", "),
        })

    # Print a sample of generated customer data for troubleshooting
    print(f"Generated Customers (start_id={start_id}):")
    print(customers[:5])  # Print only the first 5 for brevity

    return pd.DataFrame(customers)


# Generate new sales data with unique combinations of (customer_id, product_id, order_date)
def generate_sales(num_sales, customer_ids, start_order_id):
    if not customer_ids:
        print("No customer IDs available for sales generation. Exiting sales generation.")
        return pd.DataFrame()  # Return an empty DataFrame if no customer IDs are available

    sales = []
    used_combinations = set()

    for order_id in range(start_order_id, start_order_id + num_sales):
        customer_id = random.choice(customer_ids)
        product_id = random.randint(100, 500)
        order_date = fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d")

        # Ensure unique combination of (customer_id, product_id, order_date)
        while (customer_id, product_id, order_date) in used_combinations:
            customer_id = random.choice(customer_ids)
            product_id = random.randint(100, 500)
            order_date = fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d")

        used_combinations.add((customer_id, product_id, order_date))

        sales.append({
            "order_id": order_id,
            "product_id": product_id,
            "customer_id": customer_id,
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(5, 100), 2),
            "order_date": order_date,
        })

    # Print a sample of generated sales data for troubleshooting
    print(f"Generated Sales (start_order_id={start_order_id}):")
    print(sales[:5])  # Print only the first 5 for brevity

    return pd.DataFrame(sales)

# Load data into MySQL
def load_to_mysql(df, table_name):
    if df.empty:
        print(f"No data to load into {table_name} table. Skipping...")
        return

    with engine.begin() as conn:  # Use begin() to automatically commit transactions
        try:
            # Load data in chunks for efficiency
            df.to_sql(table_name, con=conn, if_exists='append', index=False, chunksize=10000)
            print(f"New data successfully loaded into {table_name} table.")
        except IntegrityError as e:
            print(f"Integrity error while loading data into {table_name} table: {e}")
        except Exception as e:
            print(f"Error while loading data into {table_name} table: {e}")

# Main function to generate and load new data
def generate_and_load_data():
    with engine.connect() as conn:
        # Get the highest customer_id and order_id to ensure uniqueness
        try:
            result = conn.execute(text("SELECT MAX(customer_id) FROM customers"))
            start_customer_id = result.scalar() or 0
            result = conn.execute(text("SELECT MAX(order_id) FROM sales"))
            start_order_id = result.scalar() or 0
        except Exception as e:
            print(f"Error fetching highest IDs from database: {e}")
            return

    # Generate new customer data
    new_customers_df = generate_customers(NUM_NEW_CUSTOMERS, start_customer_id + 1)

    # Load new customer data into MySQL
    load_to_mysql(new_customers_df, 'customers')

    # Verify the customer data was loaded successfully
    with engine.connect() as conn:
        try:
            result = conn.execute(text("SELECT COUNT(*) FROM customers"))
            customer_count = result.scalar()
            print(f"Current number of customers in database: {customer_count}")
        except Exception as e:
            print(f"Error verifying customer data in database: {e}")

    # Get customer IDs again to ensure they're available for sales generation
    # Fetch only IDs of customers who exist in the database
    with engine.connect() as conn:
        try:
            result = conn.execute(text("SELECT customer_id FROM customers WHERE customer_id > :start_id"), {'start_id': start_customer_id})
            new_customer_ids = [row[0] for row in result.fetchall()]
        except Exception as e:
            print(f"Error fetching customer IDs from database: {e}")
            return

    print(f"Customer IDs available for sales generation: {new_customer_ids[:10]}")  # Print only the first 10 for brevity

    # Generate new sales data only for the customers that have been added
    new_sales_df = generate_sales(NUM_NEW_SALES, new_customer_ids, start_order_id + 1)

    # Load new sales data into MySQL
    load_to_mysql(new_sales_df, 'sales')

    # Verify the sales data was loaded successfully
    with engine.connect() as conn:
        try:
            result = conn.execute(text("SELECT COUNT(*) FROM sales"))
            sales_count = result.scalar()
            print(f"Current number of sales in database: {sales_count}")
        except Exception as e:
            print(f"Error verifying sales data in database: {e}")

if __name__ == "__main__":
    generate_and_load_data()
