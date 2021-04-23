"""
Write a program to calculate the credit card
balance after one year if a person only pays
the minimum monthly payment required by the
credit card company each month.

For each month, calculate statements on the
monthly payment and remaining balance. At
the end of 12 months, print out the remaining
balance. Be sure to print out no more than two
decimal digits of accuracy.
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + \
              ((balance - (balance * monthlyPaymentRate))
              * (annualInterestRate/12))

print("Remaining balance:", round(balance, 2))