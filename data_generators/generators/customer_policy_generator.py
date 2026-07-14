import pandas as pd
import random
from datetime import datetime

from utils.parquet_writer import write_parquet

from config import (
    CUSTOMER_POLICY_PATH,
    SOURCE_SYSTEM,
    BATCH_ID
)


def generate_customer_policy(
        customer_df,
        policy_df,
        role_df
):

    customer_policy = []

    role_map = dict(
        zip(
            role_df["role_code"],
            role_df["role_id"]
        )
    )


    customer_ids = customer_df["customer_no"].tolist()


    customer_policy_id = 1


    for _, policy in policy_df.iterrows():


        policy_no = policy["policy_no"]


        # Policy Holder (Mandatory)

        holder = random.choice(
            customer_ids
        )


        customer_policy.append({

            "customer_policy_id":
                customer_policy_id,

            "customer_no":
                holder,

            "policy_no":
                policy_no,

            "role_id":
                role_map["PH"],

            "effective_from":
                policy["policy_start_date"],

            "effective_to":
                None,

            "relation_status":
                "ACTIVE",

            "source_system":
                SOURCE_SYSTEM,

            "batch_id":
                BATCH_ID,

            "created_date":
                datetime.now(),

            "created_by":
                "DATA_GENERATOR"

        })


        customer_policy_id += 1


        # Life Assured

        if random.random() < 0.80:

            assured = random.choice(
                customer_ids
            )


            customer_policy.append({

                "customer_policy_id":
                    customer_policy_id,

                "customer_no":
                    assured,

                "policy_no":
                    policy_no,

                "role_id":
                    role_map["LA"],

                "effective_from":
                    policy["policy_start_date"],

                "effective_to":
                    None,

                "relation_status":
                    "ACTIVE",

                "source_system":
                    SOURCE_SYSTEM,

                "batch_id":
                    BATCH_ID,

                "created_date":
                    datetime.now(),

                "created_by":
                    "DATA_GENERATOR"

            })


            customer_policy_id += 1


        # Nominee

        if random.random() < 0.70:

            nominee = random.choice(
                customer_ids
            )


            customer_policy.append({

                "customer_policy_id":
                    customer_policy_id,

                "customer_no":
                    nominee,

                "policy_no":
                    policy_no,

                "role_id":
                    role_map["NM"],

                "effective_from":
                    policy["policy_start_date"],

                "effective_to":
                    None,

                "relation_status":
                    "ACTIVE",

                "source_system":
                    SOURCE_SYSTEM,

                "batch_id":
                    BATCH_ID,

                "created_date":
                    datetime.now(),

                "created_by":
                    "DATA_GENERATOR"

            })


            customer_policy_id += 1


    df = pd.DataFrame(customer_policy)


    write_parquet(
        df,
        CUSTOMER_POLICY_PATH
    )


    return df