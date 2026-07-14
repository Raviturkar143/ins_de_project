import pandas as pd
import random
from datetime import datetime, timedelta

from utils.parquet_writer import write_parquet

from config import (
    MONEY_IN_PATH,
    MONEY_IN_COUNT,
    SOURCE_SYSTEM,
    BATCH_ID
)


def generate_money_in(policy_df):

    rows = []

    payment_id = 1


    policy_list = policy_df["policy_no"].tolist()


    for _ in range(MONEY_IN_COUNT):

        policy_no = random.choice(
            policy_list
        )


        payment_type = random.choices(
            [
                "FIRST_PREMIUM",
                "RENEWAL_PREMIUM",
                "TOPUP"
            ],
            weights=[
                0.30,
                0.60,
                0.10
            ]
        )[0]


        payment_status = random.choices(
            [
                "PAID",
                "PENDING",
                "FAILED",
                "REFUNDED"
            ],
            weights=[
                0.90,
                0.05,
                0.03,
                0.02
            ]
        )[0]


        payment_date = (
            datetime.now()
            - timedelta(
                days=random.randint(1,1500)
            )
        )


        rows.append({

            "payment_id":
                payment_id,


            "policy_no":
                policy_no,


            "installment_no":
                random.randint(
                    1,
                    20
                ),


            "payment_type":
                payment_type,


            "due_date":
                payment_date
                - timedelta(days=15),


            "payment_date":
                payment_date,


            "premium_amount":
                random.randint(
                    5000,
                    150000
                ),


            "payment_mode":
                random.choice(
                    [
                        "UPI",
                        "CARD",
                        "BANK_TRANSFER",
                        "CHEQUE"
                    ]
                ),


            "payment_status":
                payment_status,


            "transaction_reference":
                f"TXN{payment_id}{random.randint(1000,9999)}",


            "source_system":
                SOURCE_SYSTEM,


            "batch_id":
                BATCH_ID,


            "created_date":
                datetime.now(),


            "created_by":
                "DATA_GENERATOR"

        })


        payment_id += 1


    df = pd.DataFrame(rows)


    write_parquet(
        df,
        MONEY_IN_PATH
    )


    return df