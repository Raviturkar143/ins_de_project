# for local run
# Record limits

CUSTOMER_COUNT = 1000

POLICY_COUNT = 1000

AGENT_COUNT = 300

MONEY_IN_COUNT = 5000


# Batch Metadata

SOURCE_SYSTEM = "DB2_INSURANCE"

BATCH_ID = "BATCH_001"


# Output Location

OUTPUT_PATH = "../raw_data"


# Countries / Locations

CITIES = [
    "Delhi",
    "Mumbai",
    "Kolkata",
    "Bhopal",
    "Indore",
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Gondia",
    "Bhandara",
    "Nagpur",
    "Balaghat",
    "Seoni",
    "Jabalpur",
    "Wardha"
]

# ==========================
# File Paths
# ==========================

RAW_DATA_PATH = "../raw_data"

PRODUCT_PATH = f"{RAW_DATA_PATH}/product_master"
COMMISSION_PATH = f"{RAW_DATA_PATH}/product_commission_rule"
CUSTOMER_PATH = f"{RAW_DATA_PATH}/customer"
AGENT_PATH = f"{RAW_DATA_PATH}/agent"
POLICY_PATH = f"{RAW_DATA_PATH}/policy"
CUSTOMER_POLICY_PATH = f"{RAW_DATA_PATH}/customer_policy"
AGENT_POLICY_PATH = f"{RAW_DATA_PATH}/agent_policy"
MONEY_IN_PATH = f"{RAW_DATA_PATH}/money_in_dtl"


# ==========================
# Record Counts
# ==========================

CUSTOMER_COUNT = 1000
POLICY_COUNT = 1000
AGENT_COUNT = 300
MONEY_IN_COUNT = 5000


# ==========================
# Batch Metadata
# ==========================

SOURCE_SYSTEM = "DB2_INSURANCE"

BATCH_ID = "BATCH_001"


# ==========================
# Mandatory Columns
# ==========================

CUSTOMER_MANDATORY_COLUMNS = [
    "customer_no",
    "source_customer_no",
    "customer_type",
    "customer_status",
    "source_system",
    "batch_id"
]


AGENT_MANDATORY_COLUMNS = [
    "agent_no",
    "source_agent_no",
    "agent_status",
    "source_system",
    "batch_id"
]


POLICY_MANDATORY_COLUMNS = [
    "policy_no",
    "source_policy_no",
    "product_id",
    "policy_status",
    "source_system",
    "batch_id"
]


MONEY_IN_MANDATORY_COLUMNS = [
    "payment_id",
    "policy_no",
    "payment_type",
    "premium_amount",
    "payment_status",
    "source_system",
    "batch_id"
]

CUSTOMER_ROLE_PATH = f"{RAW_DATA_PATH}/customer_role_master"

AGENT_PATH = f"{RAW_DATA_PATH}/agent"

CUSTOMER_PATH = f"{RAW_DATA_PATH}/customer"

POLICY_PATH = f"{RAW_DATA_PATH}/policy"

CUSTOMER_POLICY_PATH = f"{RAW_DATA_PATH}/customer_policy"
    
AGENT_POLICY_PATH = f"{RAW_DATA_PATH}/agent_policy"

MONEY_IN_PATH = f"{RAW_DATA_PATH}/money_in_dtl"