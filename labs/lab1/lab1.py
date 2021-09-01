"""
Jonathan Neideigh
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area = ", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume = ", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the total shots: "))
    shots_made = eval(input("Enter the shots made: "))
    percentage = shots_made/total_shots * 100
    print("Shot percentage = ", percentage)

def coffee():
    lbs_purchased = eval(input("Enter the total lbs purchased: "))
    cost = 10.5*lbs_purchased + .86*lbs_purchased + 1.50
    print("Total Cost = ", cost)

def kilometers_to_miles():
    kilometers = eval(input("Enter kilometers traveled: "))
    miles = kilometers/1.61
    print("Number of Miles: ", miles)

