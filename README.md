# ins_de_project

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
│   └── requirements.txt
│
│
├── ddl/
│
├── raw_data/                    <-- Generated parquet files (local testing)
│
├── pyspark/
│                              <-- Actual ETL pipelines
│
├── target/
│                              <-- Processed output
│
├── validation/
│
├── docs/
│
└── project.md                  <-- Created after pipeline completion