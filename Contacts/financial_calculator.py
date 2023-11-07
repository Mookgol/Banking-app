import math

while True:
    print("Welcome to the Financial Calculator!")
    print("Choose a calculation: 'Investment' or 'Bond'")
    user_choice = input("Enter your choice: ").strip().lower()

    if user_choice == 'investment':
        principal = float(input("Enter the amount of money you are depositing: "))
        interest_rate = float(input("Enter the interest rate (as a decimal): "))
        years = int(input("Enter the number of years you plan on investing for: "))
        interest_type = input("Do you want 'simple' or 'compound' interest? ").strip().lower()

        if interest_type == 'simple':
            # Calculate simple interest for investment
            interest_amount = principal * (1 + interest_rate * years)
            print(f"Your total amount after {years} years with simple interest will be: {interest_amount:.2f}")

        elif interest_type == 'compound':
            # Calculate compound interest for investment
            compound_interest = principal * math.pow((1 + interest_rate), years)
            print(f"Your total amount after {years} years with compound interest will be: {compound_interest:.2f}")

        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")

    elif user_choice == 'bond':
        present_value = float(input("Enter the present value of the house: "))
        annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        years = int(input("Enter the number of years over which the bond will be repaid: "))

        monthly_interest_rate = (annual_interest_rate / 100) / 12
        total_payments = years * 12

        # Calculate monthly repayment using the provided formula
        repayment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate) ** -total_payments)
        print(f"You will have to repay approximately {repayment:.2f} each month for the bond.")

    else:
        print("Invalid choice. Please enter 'Investment' or 'Bond'.")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if another_calculation != 'yes':
        print("Thank you for using the Financial Calculator. Goodbye!")
        break