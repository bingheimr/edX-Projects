"""
Now write a program that calculates the minimum
fixed monthly payment needed in order pay off a
credit card balance within 12 months. By a fixed
monthly payment, we mean a single number which
does not change each month, but instead is a
constant amount that will be paid each month.

The program should print out one line: the
lowest monthly payment that will pay off all
debt in under 1 year, for example:

'Lowest Payment: 180'

Assume that the interest is compounded monthly
according to the balance at the end of the month
(after the payment for that month is made). The
monthly payment must be a multiple of $10 and is
the same for all months. Notice that it is possible
for the balance to become negative using this payment
scheme, which is okay.
"""

balance = 3329
annualInterestRate = 0.2

tempbalance = ''
initial_balance = balance
monthly_payment = 10


i = 1

while initial_balance > 0:
    for i in range(12):
        tempbalance = initial_balance - monthly_payment + (initial_balance - monthly_payment)*(annualInterestRate/12.0)
        initial_balance = tempbalance
        i += 1
    if initial_balance <= 0:
        print("Lowest Payment:", round(monthly_payment, 0))
        break
    else:
        tempbalance = ''
        initial_balance = balance
        monthly_payment += 10
        i = 1
