from generators.product_generator import (
    generate_product_master,
    generate_commission_rule
)

from generators.customer_role_generator import (
    generate_customer_roles
)

from generators.agent_generator import (
    generate_agents
)

from generators.customer_generator import (
    generate_customers
)

from generators.policy_generator import (
    generate_policies
)

from generators.customer_policy_generator import (
    generate_customer_policy
)

from generators.agent_policy_generator import (
    generate_agent_policy
)

from generators.money_in_generator import (
    generate_money_in
)



def main():


    print("Generating Product Master...")
    product_df = generate_product_master()


    print("Generating Commission Rules...")
    generate_commission_rule(
        product_df
    )


    print("Generating Customer Roles...")
    role_df = generate_customer_roles()


    print("Generating Agents...")
    agent_df = generate_agents()


    print("Generating Customers...")
    customer_df = generate_customers()


    print("Generating Policies...")
    policy_df = generate_policies(
        product_df
    )


    print("Generating Customer Policy Mapping...")
    generate_customer_policy(
        customer_df,
        policy_df,
        role_df
    )


    print("Generating Agent Policy Mapping...")
    generate_agent_policy(
        agent_df,
        policy_df
    )


    print("Generating Money In Transactions...")
    generate_money_in(
        policy_df
    )


    print("Data generation completed successfully.")



if __name__ == "__main__":

    main()