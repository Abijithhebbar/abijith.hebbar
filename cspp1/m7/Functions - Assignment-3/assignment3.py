"""# You'll notice that in Problem 2, your monthly payment had to be a
 multiple of $10. Why did we cent amount (in other words, the monthly
  payment is a multiple of $0.01).
# Does your code still work? It should, but you may notice that your
 code runs more slowly,
 especially in cases with very large bals and interest rates.
  (Note: when your code is
 running on our servers, there are limits on the amount of computing
  time each submission
# is allowed, so your observations from running this experiment on the grading system might be
limited to an error message complaining about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment
 than we did in Problem 2 without running into the problem of slow
# code?
# We can make this program run faster using a technique introduced in lecture - bisection search!

# The following variables contain values as described below:
# bal - the outstanding bal on the credit card
# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment such
 that we can pay off the entire bal within a year. What
# is a reasonable lower bound for this payment value? $0 is the obvious anwer,
 but you can do better than that. If there was no interest,
# the debt can be paid off by monthly payments of one-twelfth of the original
 bal, so we must pay at least this much every month.
# One-twelfth of the original bal is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid
 off the entire bal at the end of the year. What we
# ultimately pay must be greater than what we would've paid in monthly installments,
 because the interest was compounded on the bal
# we didn't pay off each month. So a good upper bound for the
 monthly payment would be one-twelfth of the bal, after having its
# interest compounded monthly for an entire year."""
def paying_debt_off_in_a_year(bal, annual_int_rate):
    """# In short:
    # Monthly interest rate = (Annual interest rate) / 12.0
    # Monthly payment lower bound = bal / 12
    # Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
    # Write a program that uses these bounds and bisection search (for more info check
     out the Wikipedia page on bisection search) to find
    # the smallest monthly payment to the cent (no more multiples of $10) such that we
     can pay off the debt within a year. Try it out with
    # large inputs, and notice how fast it is (try the same large inputs in your solution to Problem
     2 to compare!). Produce the same return
    # value as you did in Assignment 2."""
    month_int_rate = (annual_int_rate) / 12.0
    month_pay_lower_bound = bal / 12
    month_pay_up_bound = (bal * (1 + month_int_rate)**12) / 12.0
    new_bal = bal
    epsilon = 0.0001
    guess = (month_pay_lower_bound + month_pay_up_bound)/2
    while True:
        month = 1
        while month <= 12:
            new_bal = new_bal - guess
            new_bal = new_bal + (month_int_rate * new_bal)
            month += 1
        if new_bal > 0 and new_bal > epsilon:
            month_pay_lower_bound = guess
            new_bal = bal
        elif new_bal < 0 and new_bal < -epsilon:
            month_pay_up_bound = guess
            new_bal = bal
        else:
            return guess

        guess = (month_pay_lower_bound + month_pay_up_bound)/2
def main():
    """ it is a main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(round(paying_debt_off_in_a_year(data[0], data[1]), 2)))
if __name__ == "__main__":
    main()
