"""
Jonathan Neideigh

mean.py

This assignment calculates three types of means

I certify that this assignment is entirely my work
"""
import math
# this program will ask for 5 inputs and then do arithmetic and put out three different outputs
# the inputs will be how many values entered, the outputs will be the different kinds of means
#ask for num of values, ask for first through n many values, output the rms, geo and harm means

def main():
    values = eval(input("Enter the values to be entered "))
    acc = 0
    acc2 = 0
    acc3 = 1
    for i in range(values):
        total = eval(input("Enter value " + str(i + 1) + ": "))
        acc = acc + (total ** 2)
        mean = acc / values
        rms_average = math.sqrt(mean)
        acc2 = acc2 + 1 / total
        harmonic_mean = values / acc2
        acc3 = acc3 * total
        geometric_mean = acc3 ** (1/values)
    rms_average2 = round(rms_average, 3)
    harmonic_mean2 = round(harmonic_mean, 3)
    geometric_mean2 = round(geometric_mean, 3)
    print(rms_average2)
    print(harmonic_mean2)
    print(geometric_mean2)
