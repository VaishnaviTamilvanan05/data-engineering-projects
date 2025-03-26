# 🌦️ Weather Data ETL Pipeline

## Overview
The **Weather Data ETL Pipeline** is a robust solution designed to automate the daily extraction, transformation, and loading (ETL) of weather data from the Open-Meteo API into a PostgreSQL database. This project provides a streamlined approach to retrieving and structuring weather data for effective analysis, offering valuable insights into the climate of London.

## Technologies Used
- **Apache Airflow**: For orchestrating the ETL process.
- **PostgreSQL**: For structured data storage and management.
- **Docker**: For containerizing the application, ensuring consistent deployment.
- **Open-Meteo API**: The source of real-time weather data.
- **DBeaver**: For data visualization and management.

## Key Features
- **Automated Data Extraction**: Leverages Apache Airflow’s HttpHook to seamlessly pull weather data from the Open-Meteo API on a daily basis.
- **Data Transformation**: Efficiently processes the retrieved JSON data, converting it into a structured format suitable for storage in PostgreSQL.
- **Data Loading**: Utilizes Airflow’s PostgresHook to load the transformed data into a PostgreSQL database, ensuring quick access and retrieval.
- **Insightful Visualization**: Integrates with DBeaver for interactive data visualization, allowing users to analyze weather trends and patterns effortlessly.
- **Seamless Deployment**: Docker containers ensure that the application runs consistently across various environments, simplifying the setup process.

## Project Workflow
1. **Extraction**: The pipeline automatically extracts daily weather data from the Open-Meteo API, ensuring up-to-date information.
2. **Transformation**: The raw JSON data is transformed into a structured format, making it suitable for database storage and further analysis.
3. **Loading**: Transformed data is efficiently loaded into a PostgreSQL database, where it can be easily accessed for reporting and analytics.
4. **Visualization**: Utilize DBeaver to visualize the data, providing clear insights into temperature variations, wind patterns, and overall weather trends.

## Getting Started
To run this project locally, follow these steps:

### Clone the Repository:
```sh
git clone <repository-url>
cd <repository-directory>
```

### Set Up Docker:
Ensure Docker is installed and running on your machine.

### Configure Airflow:
- Create an Airflow connection for the Open-Meteo API.
- Set up the PostgreSQL connection with the necessary credentials.

### Start the Pipeline:
- Launch your Airflow instance.
- Trigger the `weather_etl_pipeline` DAG to start the ETL process.

## Conclusion
This **Weather Data ETL Pipeline** project showcases proficiency in building scalable data pipelines using modern technologies like **Apache Airflow, PostgreSQL, and Docker**.

