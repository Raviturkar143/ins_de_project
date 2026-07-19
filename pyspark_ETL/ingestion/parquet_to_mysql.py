# for single table
'''from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("InsuranceRawLoad") \
    .getOrCreate()


customer_df = spark.read.parquet(
    "raw_data/customer"
)


customer_df.write \
    .format("jdbc") \
    .option(
        "url",
        "jdbc:mysql://localhost:3306/insurance_stg"
    ) \
    .option(
        "dbtable",
        "customer_stg"
    ) \
    .option(
        "user",
        "root"
    ) \
    .option(
        "password",
        "password"
    ) \
    .mode("append") \
    .save()
'''
# for all tables 
from pyspark.sql import SparkSession

# 1. Initialize Spark with   MySQL/MariaDB driver package
spark = SparkSession.builder \
    .appName("Insurance_data_RawLoad") \
    .config("spark.jars.packages", "org.mariadb.jdbc:mariadb-java-client:3.1.4") \
    .getOrCreate()
    
# 2. Database connection configurations
url = "jdbc:mysql://localhost:3306/insurance_stg"
connection_properties = {
    "user": "root",
    "password": "####",
    "driver": "org.mariadb.jdbc.Driver",
    "batchsize": "5000",               # Speeds up inserts by grouping rows
    "rewriteBatchedStatements": "true"  # Drastically reduces network roundtrips
}

# 3.  Source Parquet Folder -> Target MySQL Table
tables = {
    "product_master": "product_master_stg",
    "product_commission_rules": "product_commission_rules_stg",
    "customer": "customer_stg",
    "agent": "agent_stg",
    "policy": "policy_stg",
    "customer_role_master": "customer_role_master_stg",
    "agent_policy": "agent_policy_stg",
    "customer_policy": "customer_policy_stg",
    "money_in_dtl": "money_in_dtl_stg"
}

# 4. Process all tables sequentially
for index, (source, target) in enumerate(tables.items(), 1):
    print(f"[{index}/9] Processing: raw_data/{source} ➔ MySQL: {target}...")
    
    try:
        # Read the Parquet source data
        df = spark.read.parquet(f"raw_data/{source}")
        
        # Coalesce to 4 prevents Spark from opening hundreds of connections at once,
        # which would crash your local MySQL database.
        df.coalesce(4).write.jdbc(
            url=url,
            table=target,
            mode="append",
            properties=connection_properties
        )
        print(f"✓ Successfully loaded {target}.\n")
        
    except Exception as e:
        print(f"❌ FAILED to load {source}. Error: {str(e)}\n")
        continue

print("All table migration operations completed!")