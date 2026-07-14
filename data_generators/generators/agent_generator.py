from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

from utils.parquet_writer import write_parquet

from config import (
    AGENT_PATH,
    AGENT_COUNT,
    SOURCE_SYSTEM,
    BATCH_ID,
    CITIES
)


fake = Faker()


def generate_agents():

    agents = []

    for i in range(1, AGENT_COUNT + 1):

        joining_date = (
            datetime.now()
            - timedelta(days=random.randint(30, 2000))
        )

        agent_status = random.choices(
            [
                "ACTIVE",
                "INACTIVE"
            ],
            weights=[
                0.85,
                0.15
            ]
        )[0]


        city = random.choice(CITIES)


        agents.append({

            "agent_no": i,

            "source_agent_no":
                f"SRC_AGT_{10000+i}",


            "first_name":
                fake.first_name(),


            "middle_name":
                fake.first_name(),


            "last_name":
                fake.last_name(),


            "dob":
                fake.date_of_birth(
                    minimum_age=25,
                    maximum_age=60
                ),


            "gender":
                random.choice(
                    [
                        "MALE",
                        "FEMALE"
                    ]
                ),


            "mobile_no":
                fake.msisdn()[:10],


            "email":
                fake.email(),


            "joining_date":
                joining_date,


            "termination_date":
                None
                if agent_status == "ACTIVE"
                else joining_date + timedelta(
                    days=random.randint(30,500)
                ),


            "designation":
                random.choice(
                    [
                        "Insurance Advisor",
                        "Senior Advisor",
                        "Sales Manager"
                    ]
                ),


            "branch_code":
                f"BR{random.randint(100,999)}",


            "branch_name":
                f"{city} Branch",


            "city":
                city,


            "state":
                fake.state(),


            "country":
                "India",


            "agent_status":
                agent_status,


            "source_system":
                SOURCE_SYSTEM,


            "batch_id":
                BATCH_ID,


            "created_date":
                datetime.now(),


            "created_by":
                "DATA_GENERATOR"

        })


    df = pd.DataFrame(agents)


    write_parquet(
        df,
        AGENT_PATH
    )


    return df