"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search
(for more info check out the Wikipedia page on bisection search)
to find the smallest monthly payment to the cent (no more multiples
of $10) such that we can pay off the debt within a year. Try it
out with large inputs, and notice how fast it is (try the same
large inputs in your solution to Problem 2 to compare!). Produce
the same return value as you did in Problem 2.

Note that if you do not use bisection search, your code will not
run - your code only has 30 seconds to run on our servers.
"""

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0

epsilon = .02
lowerbound = balance/12
upperbound = (balance * (1 + monthlyInterestRate)**12)/12.0
midpoint = (upperbound + lowerbound)/2.0

tempBalance = balance

while abs(tempBalance) >= epsilon:
    tempBalance = balance
    for i in range(12):
        unpaidBalance = tempBalance - midpoint
        monthlyInterest = (annualInterestRate/12.0)*unpaidBalance
        tempBalance = unpaidBalance + monthlyInterest
    if tempBalance > 0:
        lowerbound = midpoint
    else:
        upperbound = midpoint
    midpoint = (upperbound + lowerbound)/2.0

print("Lowest Payment is:", round(midpoint, 2))