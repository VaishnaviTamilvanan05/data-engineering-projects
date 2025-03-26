# 🏅 Tokyo 2021 Olympic Data Pipeline

## 🚀 Project Overview

A data pipeline built to transform and analyze Tokyo 2021 Olympic data using **Databricks** and **PySpark**. This project processes datasets related to athletes, teams, medals, and gender participation, providing key insights into the event.

## 🔑 Key Features

- ⚡ **Efficient Data Ingestion**: Seamlessly load large datasets from Azure Blob Storage into Databricks.
- 🔄 **Data Transformation**: Clean and process data, including type casting and calculating key metrics.
- 🏅 **Medal Analysis**: Identify top countries based on gold medals.
- 📊 **Gender Participation Insights**: Calculate average male and female participation per event.

## 🛠️ Tech Stack

- 🧠 **Databricks**: For scalable data ingestion and transformation.
- 🔥 **PySpark**: Handling big data transformations and analysis.

## 📂 Datasets

- 🏃 **Athletes**: Details on all Olympic participants.
- 🏆 **Medals**: Medal counts and distribution by country.
- 👥 **Teams**: Information on Olympic teams.
- 🧑‍🤝‍🧑 **Coaches**: Coaches' data.
- ⚖️ **Entries Gender**: Gender breakdown across events.

## 🏗️ Pipeline Workflow

1. **Data Ingestion**: 🗂️ Import raw data from Azure Blob Storage into Databricks.
2. **Transformation**:
   - Cast gender participation data columns to integers.
   - Calculate average gender participation per discipline.
   - Sort countries by gold medal count.
3. **Data Export**: Export transformed data back to Blob Storage in CSV format for further analysis.

## 📈 Results

- 🚀 **Top Countries by Gold Medals**: Easily identify leading countries.
- ⚖️ **Gender Participation Metrics**: Gain insights into gender distribution in Olympic events.

## 🌟 Future Plans

- 📊 **Visualization Dashboards**: Integrate with Power BI for real-time insights.
- 🔄 **Automated Data Feeds**: Handle live data updates for future Olympic events.
