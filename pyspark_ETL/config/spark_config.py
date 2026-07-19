from pyspark.sql import SparkSession


def get_spark_session():

    spark = (
        SparkSession.builder
        .appName(
            "Insurance_Data_Engineering"
        )

        .config(
            "spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.4.1"
        )

        .getOrCreate()
    )

    spark.sparkContext.setLogLevel(
        "WARN"
    )

    return spark