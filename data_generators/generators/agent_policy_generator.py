import pandas as pd
import random
from datetime import datetime

from utils.parquet_writer import write_parquet

from config import (
    AGENT_POLICY_PATH,
    SOURCE_SYSTEM,
    BATCH_ID
)


def generate_agent_policy(agent_df, policy_df):

    rows = []

    agent_policy_id = 1

    agent_ids = agent_df["agent_no"].tolist()


    for _, policy in policy_df.iterrows():

        primary_agent = random.choice(agent_ids)

        rows.append({

            "agent_policy_id": agent_policy_id,

            "agent_no": primary_agent,

            "policy_no": policy["policy_no"],

            "agent_role": "PRIMARY",

            "allocation_percentage": 100,

            "effective_from": policy["policy_start_date"],

            "effective_to": None,

            "relation_status": "ACTIVE",

            "source_system": SOURCE_SYSTEM,

            "batch_id": BATCH_ID,

            "created_date": datetime.now(),

            "created_by": "DATA_GENERATOR"

        })

        agent_policy_id += 1


        # Writing agents

        if random.random() < 0.40:

            writing_count = random.randint(1, 2)

            writing_agents = random.sample(
                agent_ids,
                writing_count
            )


            for agent in writing_agents:

                rows.append({

                    "agent_policy_id": agent_policy_id,

                    "agent_no": agent,

                    "policy_no": policy["policy_no"],

                    "agent_role": "WRITING",

                    "allocation_percentage": random.choice(
                        [10,20,30]
                    ),

                    "effective_from": policy["policy_start_date"],

                    "effective_to": None,

                    "relation_status": "ACTIVE",

                    "source_system": SOURCE_SYSTEM,

                    "batch_id": BATCH_ID,

                    "created_date": datetime.now(),

                    "created_by": "DATA_GENERATOR"

                })

                agent_policy_id += 1


    df = pd.DataFrame(rows)


    write_parquet(
        df,
        AGENT_POLICY_PATH
    )


    return df