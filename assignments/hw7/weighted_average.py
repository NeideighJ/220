"""
Jonathan Neideigh

weighted_average.py

This program calculates the weighted average of a class's grades

I hereby certify that this assignment is entirely my work
"""


def weighted_average():

    out_file = open("avg.txt", 'w')
    class_average = 0
    acc = 0

    with open("grades.txt") as ca:
        values = ca.readlines()

        for line in values:
            acc += 1
            split = line.split(":")
            sent = split[1]
            split1 = sent.split()
            acc1 = 0
            for i in range(0, len(split1), 2):
                acc1 += eval(split1[i])
            if acc1 > 100:
                out_file.write(split[0] + "Error: The weight is over 100" + "\n")
            elif acc1 < 100:
                out_file.write(split[0] + "Error: The weight is less than 100" + "\n")
            else:
                acc2 = 0
                for x in range(0, len(split1), 2):
                    acc2 += eval(split1[x]) * eval(split1[x+1])
                acc2 = acc2 / 100
                class_average += acc2
                out_file.write(split[0])
                out_file.write(str(acc2) + "\n")
        class_average = class_average / acc
        out_file.write("The class average is: " + str(class_average))

