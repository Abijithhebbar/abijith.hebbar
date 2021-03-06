"""
# Now write a program that calculates the minimum fixed monthly payment needed
#in order pay off a credit card balwithin 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month,but instead
# is a constant amount that will be
# paid each month
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# The program should print out one line: the lowest monthly payment that will
# pay off all debt in under 1 year, for example:
# Lowest Payment: 180"""
def paying_debt_off_in_a_year(inp_bal, annual_interest_rate):
    """# Assume that the interest is compounded monthly according to the balance
    #at the end of the month (after the payment for that month is made).
    #The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is
    # possible for the balance to become
    # negative using this payment scheme, which is okay.
    # A summary of the required math is found below:
    # Monthly interest rate = (Annual interest rate) / 12.0
    # Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate
     x Monthly unpaid balance)"""
    month_pay = 0
    bal = inp_bal
    while bal > 0:
        bal = inp_bal
        month_pay = month_pay + 10
        month = 1
        while month <= 12:
            month_intrest_rate = (annual_interest_rate) / 12.0
            monthly_unpaid_bal = (bal) - (month_pay)
            updated_balance_each_month = (monthly_unpaid_bal) + \
            (month_intrest_rate* monthly_unpaid_bal)
            bal = updated_balance_each_month
            month += 1
    return month_pay
def main():
    """ it is a main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(paying_debt_off_in_a_year(data[0], data[1])))
if __name__ == "__main__":
    main()
