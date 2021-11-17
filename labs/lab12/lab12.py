"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import randint


def farf(lst,value):
    try:
        i = lst.index(value)
        lst[i] = "Jonathan Neideigh"
    except:
        pass


def rd(filename):
    f = open(filename,"r")
    d = f.readline()
    d = d.split()
    i = 0
    while i < len(d):
        d[i] = int(d[i])
        i += 1
    return d


def iil(value,lst):
    i = 0
    while i < len(lst):
        if value == lst[i]:
            return True
        i +=1
    return False


def gi():
    x = eval(input("Enter a num in the range 1 - 10 : "))
    while x not in range(1,10):
        x = eval(input("Enter a num in the range 1 - 10 : "))
    return x


def nd():
    x = eval(input("Input a positive integer: "))
    while x > 0:
        i = 0
        while x != 0:
            i += 1
            x //= 10
        print("The number of digits is : ", i)
        x = eval(input("Input a positive integer: "))


def hl():
    number = randint(1,100)
    x = eval(input("Enter a number between 1 and 100: "))
    guesses = 0
    while x != number and guesses < 7:
        if x > number :
            print("Number is too high")
            x = eval(input("Enter another number between 1 & 100: "))
        elif x < number :
            print("Number is too low")
            x = eval(input("Enter another number between 1 & 100: "))
        guesses += 1
    if x == number:
        print("You win!")
    else:
        print("You lose :( ")


def main():
    farf([1,3,4,6,9,10],3)
    rd("datasorted")
    iil()
    gi()
    nd()
    hl()
    pass


main()
