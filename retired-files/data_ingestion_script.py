import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import text

# MySQL connection details
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/ecommerce')

try:
    # Establish a connection using SQLAlchemy engine
    with engine.connect() as conn:
        trans = conn.begin()

        customers_df = pd.read_json("customers_data.json")
        customers_df.to_sql("customers", con=conn, if_exists="append", index = False)

        sales_df = pd.read_csv("sales_data.csv")
        sales_df.to_sql("sales", con=conn, if_exists="append", index=False)

        trans.commit()

        print("Data from customers_data.json and sales_data.csv successfully inserted into customers and sales tables.")

except Exception as e:
    print(f"An error occurred: {e}")