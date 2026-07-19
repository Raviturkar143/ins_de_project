"""
Application Configuration
"""

# ==========================================================
# AWS Configuration
# ==========================================================

 

AWS_REGION = "ap-south-1"

S3_BUCKET_NAME = "insurance-data-lake-ravi"

RAW_LAYER = "raw_data"

# ==========================================================
# MySQL Configuration
# ==========================================================

MYSQL_HOST = "localhost"

MYSQL_PORT = "3306"

MYSQL_DATABASE = "insurance_stg"

MYSQL_USERNAME = "root"

MYSQL_PASSWORD = "password"


# ==========================================================
# Application Configuration
# ==========================================================

APP_NAME = "Insurance Data Engineering"

SOURCE_SYSTEM = "DB2_INSURANCE"

BATCH_ID = "BATCH_001"


# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = "INFO"

LOG_PATH = "logs/application.log"