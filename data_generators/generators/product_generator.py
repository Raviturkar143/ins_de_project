import pandas as pd
from datetime import datetime

from utils.parquet_writer import write_parquet
from config import (
    PRODUCT_PATH,
    COMMISSION_PATH,
    SOURCE_SYSTEM,
    BATCH_ID
)


def generate_product_master():

    products = [

        (101, "LIFE_TERM", "Term Life Insurance", "Life"),
        (102, "LIFE_WHOLE", "Whole Life Insurance", "Life"),
        (103, "LIFE_ENDOW", "Endowment Plan", "Life"),
        (104, "LIFE_ULIP", "ULIP Plan", "Life"),
        (105, "LIFE_CHILD", "Child Education Plan", "Life"),

        (106, "HLTH", "Health Insurance", "Health"),

        (107, "MOTOR", "Motor Insurance", "General"),
        (108, "TRAVEL", "Travel Insurance", "General"),
        (109, "PA", "Personal Accident Insurance", "General"),

        (110, "RETIRE", "Retirement Plan", "Life")
    ]


    rows = []

    for p in products:

        rows.append({

            "product_id": p[0],
            "product_code": p[1],
            "product_name": p[2],
            "product_category": p[3],

            "policy_term_years": 10,

            "premium_frequency": "YEARLY",

            "product_status": "ACTIVE",

            "source_system": SOURCE_SYSTEM,

            "batch_id": BATCH_ID,

            "created_date": datetime.now(),

            "created_by": "DATA_GENERATOR"

        })


    df = pd.DataFrame(rows)

    write_parquet(
        df,
        PRODUCT_PATH
    )

    return df



def generate_commission_rule(product_df):

    commission = {

        101:(40,9),
        102:(35,7),
        103:(30,6),
        104:(12,5),
        105:(20,5),

        106:(18,18),

        107:(15,15),
        108:(10,10),
        109:(12,12),

        110:(18,6)

    }


    rows=[]


    for _,row in product_df.iterrows():

        first,renewal = commission[row.product_id]


        rows.append({

            "commission_rule_id":
                row.product_id,

            "product_id":
                row.product_id,

            "first_year_pct":
                first,

            "renewal_pct":
                renewal,

            "effective_from":
                datetime(2026,1,1),

            "rule_status":
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


    df=pd.DataFrame(rows)


    write_parquet(
        df,
        COMMISSION_PATH
    )


    return df