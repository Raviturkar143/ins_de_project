import pandas as pd
from datetime import datetime

from utils.parquet_writer import write_parquet

from config import (
    SOURCE_SYSTEM,
    BATCH_ID,
    CUSTOMER_ROLE_PATH
)


def generate_customer_roles():

    roles = [

        (1, "PH", "POLICY HOLDER"),

        (2, "LA", "LIFE ASSURED"),

        (3, "NM", "NOMINEE"),

        (4, "AP", "APPOINTEE")

    ]


    data=[]


    for role in roles:

        data.append({

            "role_id":
                role[0],

            "role_code":
                role[1],

            "role_name":
                role[2],

            "role_status":
                "ACTIVE",

            "source_system":
                SOURCE_SYSTEM,

            "batch_id":
                BATCH_ID,

            "created_date":
                datetime.now()

        })


    df=pd.DataFrame(data)


    write_parquet(
        df,
        CUSTOMER_ROLE_PATH
    )


    return df