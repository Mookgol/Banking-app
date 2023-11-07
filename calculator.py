import math

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return principal * (1 + rate * time)

# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time):
    return principal * math.pow((1 + rate), time)

# Function to calculate bond repayment
def calculate_bond_repayment(principal, annual_rate, months):
    monthly_rate = (annual_rate / 100) / 12
    return (monthly_rate * principal) / (1 - math.pow(1 + monthly_rate, -months))

# Main function to run the program
def main():
    print("Choose either 'investment' or 'bond' to proceed:")
    choice = input().strip().lower()

    if choice == "investment":
        principal = float(input("Enter the amount of money you are depositing: "))
        rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        time = int(input("Enter the number of years you plan on investing for: "))
        interest_type = input("Do you want 'simple' or 'compound' interest? ").strip().lower()

        if interest_type == "simple":
            result = calculate_simple_interest(principal, rate, time)
        elif interest_type == "compound":
            result = calculate_compound_interest(principal, rate, time)
        else:
            print("Invalid interest type. Please choose 'simple' or 'compound'.")
            return

        print(f"Your investment will be worth: {result:.2f}")

    elif choice == "bond":
        principal = float(input("Enter the present value of the house: "))
        annual_rate = float(input("Enter the annual interest rate: "))
        months = int(input("Enter the number of months to repay the bond: "))

        repayment = calculate_bond_repayment(principal, annual_rate, months)
        print(f"Your monthly bond repayment will be: {repayment:.2f}")

    else:
        print("Invalid choice. Please choose 'investment' or 'bond'.")

if __name__ == "__main":
    main()
