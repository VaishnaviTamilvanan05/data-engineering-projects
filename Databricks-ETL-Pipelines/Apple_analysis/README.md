# 📊 Customer Analytics on Apple Product Purchases using Modular ETL Design  
### Built with Factory Pattern, PySpark, and Delta Lake on Databricks

## 🧠 Project Overview

This project demonstrates a **modular, scalable ETL pipeline** built on **Databricks** using **PySpark**, designed to analyze customer purchase behavior of **Apple products**. The pipeline processes data from multiple formats (CSV, Parquet, Delta) and provides insights into customer journeys — particularly identifying users who purchased **AirPods after buying iPhones**.

By leveraging the **Factory Design Pattern**, the project ensures high flexibility and maintainability, while utilizing modern data engineering concepts like **Delta Lake**, **broadcast joins**, **window functions**, and **data partitioning**.

---

## 🏗️ Architecture & Workflow

The ETL pipeline is broken into three modular components:

- **Extractor**: Reads input data from various sources using the Factory Pattern.
- **Transformer**: Applies business logic using PySpark DataFrame API and Spark SQL.
- **Loader**: Loads the final datasets into both **Data Lake** and **Lakehouse (Delta Table)**.

There are two workflows:
1. `FirstWorkFlow`: Extracts customers who bought AirPods after iPhone purchase.
2. `SecondWorkFlow`: Filters and loads only AirPods and iPhone-related data for targeted analysis.

---

## ⚙️ Key Technologies & Concepts

- **Databricks** (Notebook environment & orchestration)
- **Apache Spark with PySpark**
- **Delta Lake / Data Lakehouse**
- **Factory Design Pattern** for source abstraction
- **Window Functions** (`LAG`, `LEAD`) for sequential purchase logic
- **Broadcast Joins**, **Bucketing**, **Partitioning**
- **Spark SQL & DataFrame APIs**

---

## 📁 Data Sources

- Sample Apple transaction data (CSV, Parquet, Delta)
- Simulated datasets representing customer purchases over time

---

## 🔍 Business Insights Generated

- Customers who bought **AirPods after purchasing iPhones**
- Purchase sequences and customer behavior patterns
- Filtered datasets of key product pairings (iPhone + AirPods)

---

## 📈 Why This Project?

This project showcases a real-world data engineering pipeline:
- Combines clean coding practices with business relevance
- Demonstrates **modular design**, **reusability**, and **performance optimization**
- Ideal for teams working on **customer analytics**, **sales journey insights**, or **modern data platforms**

---

## 🚀 Getting Started

To run this project:
1. Import the code into a **Databricks workspace**
2. Upload the source datasets (CSV, Parquet, or Delta format)
3. Run `WorkFlowRunner` with your selected workflow name:
   ```python
   name = "firstWorkFlow"
   workFlowRunner = WorkFlowRunner(name).runner()

