"""
Name: Jonathan Neideigh
Partner: <your partner's name goes here – first and last>
lab7.py
"""

import math

def cash_conversion():
    x = eval(input("Input an integer: "))
    print("${:.2f}".format(x))

def encode():
    st = input("Input a string: ")
    key = eval(input("Input the key: "))
    acc = ""
    for c in st:
        x = ord(c)
        shift = x + key
        nc = chr(shift)
        acc = acc + nc
    print(acc)

def sphere_area(radius):
    a = 4 * math.pi * (radius ** 2)
    return a

def sphere_volume(radius):
    v = (4/3) * math.pi * (radius ** 3)
    return v

def sum_n(n):
    acc = 0
    for i in range(n):
        acc = i + acc
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = (acc + i ** 3 )
    return acc

def encode_better():
    s = input("Input a string: ")
    k = input("Input the key: ")
    acc = ""
    for i in range(len(s)):
        c = s[i]
        key = k[i%len(k)]
        key = ord(key) - 97
        shift = ord(c) + key
        nc = chr(shift)
        acc = acc + nc
    print(acc)

def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(2))
    print(sum_n(5))
    print(sum_n_cubes(7))
    encode_better()
    pass


main()
