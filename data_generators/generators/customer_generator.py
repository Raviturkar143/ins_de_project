from faker import Faker
import pandas as pd
import random
from datetime import datetime

from utils.parquet_writer import write_parquet

from config import (
    CUSTOMER_PATH,
    CUSTOMER_COUNT,
    SOURCE_SYSTEM,
    BATCH_ID,
    CITIES
)


fake = Faker()


def generate_customers():

    customers = []


    for i in range(1, CUSTOMER_COUNT + 1):

        customer_type = random.choices(
            [
                "INDIVIDUAL",
                "CORPORATE"
            ],
            weights=[
                0.80,
                0.20
            ]
        )[0]


        city = random.choice(CITIES)


        if customer_type == "INDIVIDUAL":

            first_name = fake.first_name()
            middle_name = fake.first_name()
            last_name = fake.last_name()

            company_name = None

            dob = fake.date_of_birth(
                minimum_age=18,
                maximum_age=75
            )

            gender = random.choice(
                [
                    "MALE",
                    "FEMALE"
                ]
            )


        else:

            first_name = None
            middle_name = None
            last_name = None

            company_name = (
                fake.company()
                + " Pvt Ltd"
            )

            dob = None
            gender = None


        customer_status = random.choices(
            [
                "ACTIVE",
                "INACTIVE",
                "DECEASED"
            ],
            weights=[
                0.85,
                0.10,
                0.05
            ]
        )[0]


        customers.append({

            "customer_no":
                i,


            "source_customer_no":
                f"SRC_CUST_{10000+i}",


            "customer_type":
                customer_type,


            "first_name":
                first_name,


            "middle_name":
                middle_name,


            "last_name":
                last_name,


            "company_name":
                company_name,


            "dob":
                dob,


            "gender":
                gender,


            "mobile_no":
                fake.msisdn()[:10],


            "email":
                fake.email(),


            "national_id":
                fake.bothify(
                    text="##########"
                ),


            "pan_number":
                fake.bothify(
                    text="?????####?"
                ).upper(),


            "occupation":
                random.choice(
                    [
                        "Engineer",
                        "Business",
                        "Teacher",
                        "Doctor",
                        "Farmer",
                        "Private Employee"
                    ]
                ),


            "annual_income":
                random.randint(
                    200000,
                    3000000
                ),


            "marital_status":
                random.choice(
                    [
                        "SINGLE",
                        "MARRIED",
                        "DIVORCED"
                    ]
                ),


            "address_line1":
                fake.street_address(),


            "address_line2":
                fake.secondary_address(),


            "city":
                city,


            "state":
                fake.state(),


            "country":
                "India",


            "postal_code":
                fake.postcode(),


            "kyc_status":
                random.choice(
                    [
                        "VERIFIED",
                        "PENDING",
                        "REJECTED"
                    ]
                ),


            "customer_status":
                customer_status,


            "source_system":
                SOURCE_SYSTEM,


            "batch_id":
                BATCH_ID,


            "created_date":
                datetime.now(),


            "created_by":
                "DATA_GENERATOR"

        })


    df = pd.DataFrame(customers)


    write_parquet(
        df,
        CUSTOMER_PATH
    )


    return df