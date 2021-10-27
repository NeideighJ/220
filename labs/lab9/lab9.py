"""
Name: Jonathan Neideigh
lab9.py
"""
from graphics import *
import math

def addTens(x):
    for i in range(len(x)):
        x[i] = x[i] + 10

def squareEach(x):
    for i in range(len(x)):
        x[i] = x[i] ** 2

def sumLists(x):
    acc = 0
    for i in range(len(x)):
        acc = acc + x[i]
    return acc

def toNumbers(x):
    for i in range(len(x)):
        x[i] = float(x[i])

def writeSumOfSquares():
    in_file = input("Enter the input file name: ")
    infile = open(in_file, "r")
    outfile = open("output.txt", "w+")
    for line in infile:
        number = line.split()
        toNumbers(number)
        squareEach(number)
        s = sumLists(number)
        outfile.write("Sum = " + str(s) + "\n")



def starter():
    weight = eval(input("What is your weight? "))
    wins = eval(input("How many wins do you have? "))
    if weight >= 150 and weight < 160 and wins >=5:
        print("This individual should start")
    elif weight > 199 or wins > 20:
        print("This individual should start")
    else:
        print("This individual should not start")

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("It is a leap year! ")
    else:
        print("It is not a leap year :( ")

def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p1.getX()-p2.getX()) ** 2 + (p1.getY()-p2.getY()) ** 2)
    circle = Circle(p1,radius1)
    circle.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle = Circle(p3, radius2)
    circle.draw(win)
    distance = ((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance < (radius1 + radius2):
        inst_pt = Point(400/2, 300)
        instructions = Text(inst_pt, "The Circles Overlap")
        instructions.draw(win)
    else:
        inst_pt = Point(400 / 2, 300)
        instructions = Text(inst_pt, "The Circles Don't Overlap")
        instructions.draw(win)

    win.getMouse()
    win.close()



def main():
    # add other function calls here
    pass


main()
