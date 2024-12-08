# Data Engineering and Visualization Pipeline

## Project Overview
This project involves building an end-to-end data engineering pipeline using **Python 3**, **AWS EC2 and RDS**, **PySpark**, and **Tableau**. The goal was to extract, transform, and load (ETL) e-commerce data from MySQL (hosted on AWS RDS), perform data transformations using PySpark, and visualize the results in Tableau.

The project demonstrates advanced **data engineering skills**, **cloud infrastructure management**, and **data visualization capabilities**, with automation and scalability at its core.

## Technologies Used 
1. **Python 3:** For ETL pipeline implementation.
2. **AWS EC2:** For hosting and running scripts in a scalable cloud environment.
3. **AWS RDS:** To store the e-commerce dataset in a MySQL database.
4. **PySpark:** For data transformation and aggregation.
5. **Tableau:** To create dashboards and visualizations.
6. **MySQL Connector:** To enable interaction between PySpark and MySQL.

---

## Thought Process Behind the Steps

### 1. Setting Up the Environment
**Objective:** Host the data and the ETL process in a cloud environment.

* **AWS EC2:** Chosen as the compute instance for running Python and PySpark scripts. EC2 provides flexibility in scaling and a reliable environment to handle the pipeline execution.
* **AWS RDS:** Selected to store the e-commerce dataset, providing a fully managed relational database.

**Challenges:**
- **Configuring AWS:** Setting up security groups, ensuring the EC2 and RDS instances were in the same VPC, and enabling public accessibility for RDS.
- **Installing Dependencies:** Downloading and configuring Python, Java (for PySpark), MySQL Connector, and other required libraries on the EC2 instance.

**Solutions:** 
- Detailed documentation for each step, such as configuring inbound rules for RDS and troubleshooting EC2 connectivity issues, ensured a smooth setup.
- Leveraged **crontab** to automate the Python script, ensuring ETL tasks ran daily.

---

### 2. Extracting and Loading Data
**Objective:** Fetch e-commerce data, load it into the database, and automate this process.

* A **Python script** was created to:
  - Generate synthetic e-commerce data using the Faker library.
  - Load the data into the **MySQL database** hosted on AWS RDS.
* The ETL pipeline was automated using **crontab** to run at midnight every day.

**Challenges:**
- Ensuring that the **MySQL schema** and tables were properly created on RDS using SQL files.
- Automating the process and validating data integrity after every run.

**Solutions:**
- Verified the schema setup and used Python’s SQLAlchemy library to ensure consistent data loading.
- Implemented automated checks for record counts and data accuracy.

---

### 3. Transforming Data with PySpark
**Objective:** Perform complex transformations and aggregations to prepare the data for visualization.

* **PySpark** was used for its scalability and efficiency in handling large datasets. Key transformations included:
  - Joining customer and sales data to enrich information.
  - Calculating **monthly revenue per customer**.
  - Aggregating total sales and revenue across time periods.

**Challenges:**
- Configuring **PySpark** on AWS EC2, including downloading and setting up the correct Spark version, Java dependencies, and Hadoop libraries.
- Connecting PySpark to MySQL using the **MySQL Connector** jar.

**Solutions:**
- Used the `spark-submit` command with the `--jars` option to include the MySQL Connector during runtime.
- Verified the transformations step-by-step using the PySpark interactive shell.

---

### 4. Visualizing Data with Tableau
**Objective:** Create interactive dashboards to visualize insights from the transformed data.

* Tableau was used to:
  - Connect to the MySQL database on AWS RDS.
  - Create visualizations such as bar charts, line graphs, and heatmaps to display trends and key metrics.
  - Build a dashboard for **monthly revenue trends** and **customer sales distribution**.

**Challenges:**
- Configuring Tableau to connect with MySQL RDS using the correct **MySQL ODBC driver**.
- Troubleshooting Tableau connectivity issues related to authentication plugins like `mysql_native_password`.

**Solutions:**
- Modified the MySQL RDS **parameter group** to use the appropriate authentication plugin.
- Installed the **Tableau MySQL driver** and verified connection parameters.

---

## Key Challenges Faced
1. **AWS Configuration:**
   - Ensuring security groups allowed connectivity between EC2 and RDS.
   - Resolving issues with public accessibility for the RDS instance.

2. **Dependency Management:**
   - Installing PySpark and Java on EC2, and configuring the correct environment variables.
   - Using the correct MySQL Connector jar to enable communication between PySpark and MySQL.

3. **Automation:**
   - Setting up **crontab** to automate the ETL process.
   - Validating that the scripts ran successfully and data was loaded as expected.

4. **Visualization Challenges:**
   - Resolving Tableau authentication issues with MySQL.
   - Designing meaningful and interactive dashboards.

---

## Future Work
1. **Adding More Visualizations:**
   - Include heatmaps, scatter plots, and time-series charts in Tableau to uncover deeper insights.
2. **Scaling the Pipeline:**
   - Introduce **AWS S3** to store intermediate data and enhance scalability.
   - Leverage **Apache Airflow** for more advanced workflow orchestration.
3. **Big Data Handling:**
   - Experiment with **AWS EMR** or **Databricks** for distributed data processing.

---

## Repository Structure
