Project Title: Automated Data Warehouse and ETL Pipeline for E-Commerce Dataset

Project Description:

This project focuses on building an automated ETL pipeline and a data warehouse for an e-commerce dataset, demonstrating core skills in data engineering, automation, and data visualization. The project includes the following components:

Data Generation: A Python script generates daily data for customer and sales transactions, simulating a real-world scenario of continuous data inflow. This provides the foundation for building a robust ETL pipeline that handles frequent data updates.

ETL Process: The ETL pipeline, implemented using Python and SQL, extracts raw data, transforms it into the desired format, and loads it into a MySQL data warehouse. The ETL process includes steps for handling new data incrementally, reducing redundancy and ensuring that the data warehouse is always up to date.

Data Warehouse: The data warehouse schema follows a star schema approach, with a dimension table (dim_customers) containing customer information and a fact table (fact_sales) containing sales transactions. This structure enables efficient querying and analysis of the data.

Automation: The ETL process is fully automated using cron jobs, which schedule the data generation and transformation tasks on a daily basis. This automation showcases the ability to build a scalable and maintainable data pipeline without manual intervention.

Data Analysis and Visualization: The project also includes the use of Tableau to create visualizations for key business metrics, such as monthly sales trends and top customer spending. These visualizations demonstrate how the data warehouse can be used to derive actionable insights for business decision-making.

Key Features:

Fully automated data generation and ETL pipeline.

Incremental data updates for efficient data warehouse maintenance.

Use of MySQL for data warehousing and schema design.

Tableau visualizations for business insights.

Demonstrates scalability, automation, and strong data engineering practices.

Technologies Used:

Python (data generation, ETL process)

MySQL (data warehouse, schema design)

Cron Jobs (automation)

Tableau (data visualization)

How to Run the Project:

Data Generation: The Python script data_generation_script.py is scheduled to run daily using a cron job. It generates new customer and sales data files (new_customers_data.json and new_sales_data.csv).

ETL Process: The ETL script (etl_pipeline_script.py) is also scheduled using a cron job to extract, transform, and load the generated data into the MySQL database.

Data Warehouse: The MySQL database stores the transformed data in dimension and fact tables, which are optimized for querying.

Visualization: Use Tableau to connect to the MySQL database and visualize the data for insights.

Usage Instructions:

Clone the repository and set up the required environment (Python, MySQL, Tableau).

Modify the cron job schedules to fit your desired frequency of data updates.

Run the Python scripts to generate and load data into the MySQL database.

Potential Extensions:

Implement real-time streaming data ingestion using Apache Kafka and Spark.

Add more complex transformation logic, such as data enrichment or deduplication.

Integrate with cloud services like AWS or GCP for scalable storage and processing.

This project showcases the complete lifecycle of data engineering, from raw data generation to automated ETL processes, data warehousing, and visual analytics. It highlights best practices in data automation, scalability, and effective data presentation for decision-making.
