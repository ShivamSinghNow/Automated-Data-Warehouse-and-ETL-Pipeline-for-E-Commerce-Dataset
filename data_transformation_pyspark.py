from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, sum, count

# Step 1: Initialize SparkSession
spark = SparkSession.builder \
    .appName("E-commerce Data Transformation") \
    .config("spark.jars", "/path/to/mysql-connector-java.jar") \
    .getOrCreate()

# Step 2: Define MySQL connection parameters
db_url = "jdbc:mysql://my-ecommerce-db.cn68aoymgc0l.us-west-1.rds.amazonaws.com:3306/ecommerce"
db_user = "shiv"
db_password = "Awesomeward15$"

# Step 3: Load customer and sales data from MySQL
customer_df = spark.read.format("jdbc") \
    .option("url", db_url) \
    .option("dbtable", "customers") \
    .option("user", db_user) \
    .option("password", db_password) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .load()

sales_df = spark.read.format("jdbc") \
    .option("url", db_url) \
    .option("dbtable", "sales") \
    .option("user", db_user) \
    .option("password", db_password) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .load()

# Step 4: Transform data
# Example Transformation 1: Join customers and sales to enrich sales data
enriched_sales_df = sales_df.join(customer_df, "customer_id", "inner")

# Example Transformation 2: Calculate monthly revenue for each customer
monthly_revenue_df = enriched_sales_df \
    .withColumn("year", year(col("order_date"))) \
    .withColumn("month", month(col("order_date"))) \
    .groupBy("customer_id", "year", "month") \
    .agg(sum("price").alias("monthly_revenue"), count("order_id").alias("order_count"))

# Step 5: Save transformed data back to MySQL (or save as Parquet file)
# Write back to a new MySQL table
monthly_revenue_df.write.format("jdbc") \
    .option("url", db_url) \
    .option("dbtable", "monthly_revenue") \
    .option("user", db_user) \
    .option("password", db_password) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .mode("overwrite") \
    .save()


# Stop the Spark session
spark.stop()
