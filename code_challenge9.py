#task1

print("\n")

loan_amount = 1000
loan_term = 2
int_rate = 0.00256
rem_bal = loan_amount
principal = loan_amount / (loan_term * 12)
interest = rem_bal * int_rate
monthly_payment = principal + interest

print(f"\nENTER AMOUNT OF LOAN: {loan_amount} \nENTER LOAN PERIOD IN YEARS: {loan_term}")

print(f" \n Payment Schedule \n | \tMonth\t\t | \tMonthly Payment\t | \tPrincipal\t | \tInterest\t | \tRemaining Balance      |")
print("--------------------------------------------------------------------------------------------------------------------------")

for x in range(1, (12*loan_term) +1):
    interest = rem_bal * int_rate
    monthly_payment = principal + interest
    rem_bal = rem_bal - principal 

    for y in range(0, 1):
        print(f" \t{x}\t\t | \t{monthly_payment:.2f}\t\t | \t{principal:.2f}\t\t | \t{interest:.2f}\t\t | \t{rem_bal:.2f} ")
    print(end="")

#task2
print("\n")

for e in range(0,7):
    for u in range(0,13):
        if e==6 or u+e==6 or u-e==6:
            print("*",end="")
        else:
            print(" ",end="")
    print()

#task3

print("\n")

for z in range(0,8):
    for a in range(0,8):
        if z == 0 or z == 7 or z+a == 7:
            print("*",end="")
        else: 
            print(" ",end="")
    print()



