#activity13

username = input("Username: ")
password = input("Password: ")
        
age = int(input("Enter age:"))
is_employed = bool(input("Are you currently employed?:"))
crdt_score = eval(input("Credit score history:"))
annual_income = eval(input("How much is your annual income?:"))
has_collateral = bool(input("Do you have any collateral?:")) 
collateral_name = input("Collateral: ")
collateral_value = float(input("Collateral value: "))

if collateral_value < 30000:
    print("Invalid collateral value")

loan_amount = bool(input("Loan amount: "))

# Baseline Eligibility
if age >= 21 and age <=65 and is_employed == "True":

    if crdt_score >= 750:
        print("Base interest rate is 5.0%")

        if annual_income >= 100000:
            print("Loyalty Discount: Your final rate is 4.5%")
        else:
            print("Final rate is 5.0%")

    elif crdt_score >= 600:
        print("Base interest rate is 8.0%")

        if has_collateral == "True":
            print("Final rate is 7.0%")

        elif annual_income < 40000:
            print("Final rate is 9.5%")

        else:
            print("Final rate is 8.0%")

    else:
        print("Rejected. Credit score too low")

else:
    print("Fails baseline criteria")
    