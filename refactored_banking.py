# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

## In demonstration of what was learned in class:
from utils import clean_input_to_float
from utils import clean_input_to_int

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance_str = input("\nPlease enter your savings account balance: ")
    savings_balance = clean_input_to_float(savings_balance_str)

    savings_interest_str = input("Please enter your savings interest rate (APR) as a percentage: ")
    savings_interest = clean_input_to_float(savings_interest_str)

    savings_maturity_str = input("Please enter the number of months you will save this money: ")
    savings_maturity = clean_input_to_int(savings_maturity_str)
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nAfter {savings_maturity} months you will have earned ${interest_earned:,.2f} and your balance will be ${updated_savings_balance:,.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    cd_balance_str = input("Please enter your CD account balance: ")
    cd_balance = clean_input_to_float(cd_balance_str)

    cd_interest_str = input("Please enter your CD interest rate (APR) as a percentage: ")
    cd_interest = clean_input_to_float(cd_interest_str)

    cd_maturity_str = input("Please enter the number of months you will save this money: ")
    cd_maturity = clean_input_to_int(cd_maturity_str)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out thpythone interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nAfter {cd_maturity} months you will have earned ${interest_earned:,.2f} and your balance will be ${updated_cd_balance:,.2f}\n")

if __name__ == "__main__":
    # Call the main function.
    main()