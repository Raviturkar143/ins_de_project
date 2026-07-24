# ins_de_projec
# 🏦 Insurance Data Engineering Project (End-to-End)

## 📌 Project Overview

This project demonstrates an end-to-end Data Engineering pipeline built using the Medallion Architecture (Bronze → Silver → Gold) on Databricks.

The project simulates a real-world Insurance Policy Administration System (PAS) migration where raw insurance data is ingested, transformed, 
and curated into business-ready datasets for reporting and analytics.

The objective is to showcase production-style Data Engineering practices including:

- Data Ingestion
- Data Cleansing
- Data Standardization
- Delta Lake
- Medallion Architecture
- Business Transformations
- Analytical Data Products
- BI Ready Outputs

---

# 🏗 Architecture

```
                    Source Parquet Files
                            │
                            ▼
                     Bronze Layer (Delta)
               Raw Data + Audit Columns
                            │
                            ▼
                    Silver Layer (Delta)
              Cleansed & Standardized Data
                            │
                            ▼
                     Gold Layer (Delta)
               Business Ready Data Products
                            │
          ┌─────────────────┴────────────────┐
          ▼                                  ▼
      Delta Tables                    CSV Exports
   (Analytics Layer)                 (BI Reporting)
```

---

# 📂 Project Structure

```text
INS_DE_PROJECT/
│
├── config/
│   ├── app_config.py
│   └── spark_config.py
│
├── DATABRICKS/
│   ├── config.py
│   ├── data_file_generator.py
│   ├── 01_bronze_ingestion
│   ├── 02_silver_transformation
│   │
│   └── Gold_Data_Mart/
│       ├── 03_agent_commission
│       └── 03_Product_sold_by_area
│
├── ingestion/
│   ├── __init__.py
│   ├── parquet_to_mysql.py
│   ├── s3_reader.py
│   └── s3_writer.py
│
├── main.py
├── requirement.txt
└── README.md
```
---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Processing | PySpark |
| Platform | Databricks | VS code (for data generator)
| Storage | Delta Lake |AWS S3
| File Format | Parquet |CSV
| Reporting | CSV |
| Version Control | Git & GitHub |

---

# 📦 Dataset

Synthetic Insurance Data was generated using Python.

Current Tables

| Table |
|---------|
| Agent |
| Agent Policy |
| Customer |
| Customer Policy |
| Customer Role Master |
| Policy |
| Product Master |
| Product Commission Rule |
| Money In Detail |

---

# Bronze Layer

### Objective

Store raw source data without applying business transformations.

### Operations

- Read Raw Parquet Files
- Add Audit Columns
    - ingestion_timestamp
    - ingestion_date
- Store as Delta Tables

Example

```
Raw Parquet
        ↓
Bronze Delta
```

---

# Silver Layer

### Objective

Perform cleansing, standardization and reusable business transformations.

### Transformations
### Agent
- Remove unnecessary columns
- Create Agent Full Name
- Create Agent Location
- Standardize schema
- Store as Delta
- 
### Customer
- Create Customer Full Name
- Remove unwanted columns
- Standardize schema
- ---
### Policy
- Retain only business-required columns
- Standardize policy data
--
### Agent Policy
- Standardize mapping data
---
### Customer Policy
- Standardize mapping data
### Product Master
- Keep only analytical columns

### Product Commission Rule
- Standardize commission rules

# Gold Layer
Business-ready datasets used directly by reporting tools.
## Pipeline 1
# Agent Incentive Calculation
### Business Requirement
Calculate commission earned by each agent based on:

- Policies Sold
- Premium Collected
- Product Commission Rules

### Final Output

| Column |
|----------|
| Agent ID |
| Policy Number |
| Agent Full Name |
| Agent Location |
| Customer Number |
| Customer Name |
| Policy Number |
| Sum Assured |
| Total Premium Till Date |
| Agent Commission |

Output Formats

- Delta
- CSV

---

## Pipeline 2

# Product Sales By City

### Business Requirement
Identify the highest selling insurance products in each city.
 ### Final Output

| Column |
|----------|
| City |
| Product Name |
| Category |
| Policies Sold |

#Output Formats

- Delta
- CSV
# Medallion Architecture

```
Parquet,CSV (Raw)
   │
   ▼
Bronze (Delta)
   │
   ▼
Silver (Delta)
   │
   ▼
Gold (Delta + CSV)(Required Format)
 
# Audit Columns

Every layer contains audit information. Also usefil for Incremental and automated Pipeline

| Column |
|---------|
| Source System |
| Batch ID |
| Created Date |
| Ingestion Timestamp |
| Ingestion Date |

---

# Features Implemented

✅ End-to-End ETL Pipeline

✅ Modular Notebook Design

✅ Delta Lake

✅ Bronze Layer

✅ Silver Layer

✅ Gold Layer

✅ Business Transformations

✅ Data Cleansing

✅ Aggregations

✅ Window Functions

✅ CSV Export

✅ Delta Export

✅ Unity Catalog Ready

---

# Future Enhancements

- Incremental Data Loading
- Automatic Triggered Pipelines(Scheduled jobs)
- Delta MERGE
- Slowly Changing Dimension (SCD Type 2)
- Data Quality Framework
- Logging Framework
- Exception Handling
- Parameterized Notebooks
- Workflow Orchestration
- Unit Testing
- CI/CD Pipeline
- Power BI Dashboard

# Author
**Ravi Turkar**
Data Engineer
Skills
- SQL
- Oracle/MySQL
- PySpark
- Databricks
- Python
- Java
- Delta Lake
- ETL
- Data Migration
- AWS
 
# # This Was The First Folder Structure I created and till Data Generator I created this into local then Moved to Databricks ↑↑↑↑
insurance-data-engineering/

│
├── data_generator/              <-- Simulates source system extracts
│   │
│   ├── generators/
│   │   ├── product_generator.py
│   │   ├── customer_generator.py
│   │   ├── agent_generator.py
│   │   ├── policy_generator.py
│   │   ├── customer_policy_generator.py
│   │   ├── agent_policy_generator.py
│   │   └── money_in_generator.py
│   │
│   ├── utils/
│   │   ├── parquet_writer.py
│   │
│   ├── config/
│   │   └── constants.py
│   │
│   ├── main.py
│   └── requirements.tx

