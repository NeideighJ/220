"""
Name: Jonathan Neideigh
interest.py

Problem: Calculates the monthly interest charge

Certification of Authenticity: I certify that this assignment is entirely my work
"""

def main():
    rate = eval(input("What is the annual interest rate? "))
    cycle = eval(input("How many days are in the billing cycle? "))
    balance = eval(input("What is the original net balance? "))
    payment = eval(input("How much is your payment? "))
    day = eval(input("What day of the billing cycle are you making your payment on "))
    step1 = balance * cycle
    step2 = payment * (cycle-day)
    step3 = step1 - step2
    daily_balance = step3 / cycle
    mir = rate / 12
    mic = daily_balance * mir
    print(round(mic*.01,2))

if __name__ == '__main__':
    main()
