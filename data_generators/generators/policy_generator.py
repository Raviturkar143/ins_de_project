from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

from utils.parquet_writer import write_parquet

from config import (
    POLICY_PATH,
    POLICY_COUNT,
    SOURCE_SYSTEM,
    BATCH_ID
)


fake = Faker()


def generate_policies(product_df):

    policies = []


    for i in range(1000, 1000 + POLICY_COUNT):

        product = product_df.sample(
            1
        ).iloc[0]


        start_date = (
            datetime.now()
            - timedelta(
                days=random.randint(30, 2000)
            )
        )


        term_years = random.choice(
            [
                5,
                10,
                15,
                20,
                25
            ]
        )


        policy_status = random.choices(

            [
                "ACTIVE",
                "LAPSED",
                "CANCELLED",
                "MATURED",
                "SURRENDERED",
                "NOT_TAKEN_UP"
            ],

            weights=[
                0.80,
                0.08,
                0.03,
                0.04,
                0.02,
                0.03
            ]

        )[0]


        policies.append({

            "policy_no":
                i,


            "source_policy_no":
                f"SRC_POL_{i}",


            "product_id":
                int(product.product_id),


            "policy_start_date":
                start_date,


            "policy_end_date":
                start_date.replace(
                    year=start_date.year + term_years
                ),


            "issue_date":
                start_date,


            "premium_frequency":
                random.choice(
                    [
                        "MONTHLY",
                        "QUARTERLY",
                        "YEARLY"
                    ]
                ),


            "premium_amount":
                random.randint(
                    5000,
                    150000
                ),


            "sum_assured":
                random.randint(
                    500000,
                    10000000
                ),


            "policy_term_years":
                term_years,


            "payment_term_years":
                term_years,


            "policy_status":
                policy_status,


            "source_system":
                SOURCE_SYSTEM,


            "batch_id":
                BATCH_ID,


            "created_date":
                datetime.now(),


            "created_by":
                "DATA_GENERATOR"

        })


    df = pd.DataFrame(policies)


    write_parquet(
        df,
        POLICY_PATH
    )


    return df