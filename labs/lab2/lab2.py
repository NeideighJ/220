"""
Name: Jonathan Neideigh
lab2.py
"""
import math
def sum_of_threes():
    bound = eval(input("Enter the upper bound: "))
    acc = 0
    for total in range(0, bound+1,3):
       acc =  total + acc

    print(acc)

def multiplication_table():
    for h in range(1,11):
        for L in range(1,11):
            print(h * L, end = " ")
        print()

def triangle_area():
    a = eval(input("Enter side a: "))
    b = eval(input("Enter side b: "))
    c = eval(input("Enter side c: "))
    s = (a + b + c)/2
    A = s * (s-a) * (s-b) * (s-c)
    A = math.sqrt(A)
    print(A)


def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent"))
    acc = 1
    for power in range(exponent):
        acc = acc * base
    print(acc)

def sumSquares():
    first = eval(input("Enter the starting number: "))
    last = eval(input("Enter the last number: "))
    acc = 0
    for square in range(first,last + 1):
        acc = square ** 2 + acc
    print(acc)