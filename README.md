# End-to-End Data Engineering Project with Apache Spark, Azure Databricks, and DBT
This project showcases a complete data engineering pipeline utilizing Apache Spark, Azure Databricks, and the Data Build Tool (DBT), with Azure serving as the cloud provider.

## Key Components:


- **Data Ingestion**
  - Set up a Data Lake using the AdventureWorks dataset, initially storing raw data in the bronze layer as Parquet files.

- **Data Integration**
  - Used Azure Data Factory to orchestrate the data flow from ingestion to transformation.

- **Data Transformation** Leveraged Azure Databricks for data processing, implementing a medallion architecture that refines data through multiple layers:
  - **Bronze Layer:** 
    - Raw data ingestion in Parquet format.
  - **Silver Layer:** 
    - Cleaned and enriched data stored in Delta format for further transformations.
  - **Gold Layer:** 
    - Aggregated and business-ready data stored in Delta format for analysis and reporting.

- **Data Modeling**
  - Utilized DBT for SQL-based data transformations and modeling within the medallion architecture.

### STORAGE ACC - MEDALLION 

![alt text](image-2.png)

### ADF pipeline

![alt text](image-1.png)

### Databricks Cluster for compute

![image](https://github.com/user-attachments/assets/75e0df0c-1fae-43a4-bfc9-fbed3690bd80)



### DBT Generated Workflow Document

Access the DBT-generated workflow document at the following URL:
[DBT Workflow Document](http://localhost:8080/#!/model/model.medallion_dbt_spark.dim_sales)

## Installation Commands for DBT Connection from IDE

For setting up DBT in your development environment using PyCharm, follow these installation commands:

- **IDE Used:** PyCharm

- **Install DBT for Databricks:** pip install dbt-databricks

- **Install Databricks CLI** pip install databricks-cli

- **Verify Databricks File System** databricks fs ls

- **Initialize DBT Project** dbt init

Try running the following dbt commands:
- dbt run
- dbt test



### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

