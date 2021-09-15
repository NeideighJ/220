"""
Name: Jonathan Neideigh
lab3.py
"""

def average():
    hw = eval(input("Enter the amount of hw assignments: "))
    acc = 0
    for i in range(hw):
        total = eval(input("Enter your grade on HW  " + str(i + 1) + ": "))
        acc = acc + total
    average = acc / hw
    print("Total hw average: " , average)

average()


def sequence():
    x = eval(input("How many terms in series? "))
    for i in range(1, x + 1):
        y = 1 + (i // 2 * 2)
        print(y, end = " ")
    print()

sequence()

def tip_jar():
    acc = 0
    for i in range(5):
        amount = eval(input("How much are you donating? "))
        acc = acc + amount
        print(acc)

tip_jar()

def newton():
    x = eval(input("What the number you're trying to find the root of: "))
    refine = eval(input("How many times would like to refine: "))
    approx = x / 2
    for i in range(refine):
        approx = ((approx + (x / approx))/2)
    print(x , approx)

newton()

def pi():
    terms = eval(input("Enter the amount of terms in the series: "))
    acc = 1
    for i in range(terms):
        num = 2 + (i//2*2)
        denom = 1 + ((i+1)//2*2)
        acc = acc * (num / denom)
    print(acc * 2)

pi()