from config.spark_config import get_spark_session
from config.app_config import S3_BUCKET_NAME, RAW_LAYER


RAW_TABLES = [
    "customer",
    "agent",
    "policy",
    "customer_policy",
    "agent_policy",
    "money_in_dtl",
    "money_out_dtl",
    "unit_history_dtl",
    "claim_dtl",
    "commission_dtl",
    "commission_payout_dtl",
    "policy_benefit_dtl",
    "product_master",
    "product_commission_rule",
    "customer_role_master"
]


def read_parquet_from_s3(spark, table_name):

    path = (
        f"s3a://{S3_BUCKET_NAME}/"
        f"{RAW_LAYER}/"
        f"{table_name}/"
    )

    print(f"Reading: {path}")

    df = spark.read.parquet(path)

    return df



def read_all_source_tables():

    spark = get_spark_session()

    source_data = {}

    for table in RAW_TABLES:

        try:
            df = read_parquet_from_s3(
                spark,
                table
            )

            source_data[table] = df

            print(
                f"{table} loaded successfully "
                f"Count: {df.count()}"
            )

        except Exception as e:

            print(
                f"Failed loading {table}"
            )

            print(e)


    return spark, source_data



if __name__ == "__main__":

    spark, tables = read_all_source_tables()


    print("\nLoaded Tables:")

    for table in tables.keys():
        print(table)


    spark.stop()