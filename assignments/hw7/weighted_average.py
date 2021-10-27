"""
Jonathan Neideigh

weighted_average.py

This program calculates the weighted average of a class's grades

I hereby certify that this assignment is entirely my work
"""

def main():
    weighted_average("grades.txt", "avg.txt")


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, 'w+')
    class_average = 0
    acc = 0
    for line in in_file:
        split = line.split(": ")
        sent = split[1]
        split1 = sent.split()
        acc1 = 0
        for i in range(0, len(split1), 2):
            acc1 += eval(split1[i])
        if acc1 > 100:
            out_file.write(split[0] + "'s average: Error: The weights are more than 100." + "\n")
        elif acc1 < 100:
            out_file.write(split[0] + "'s average: Error: The weights are less than 100." + "\n")
        else:
            acc += 1
            acc2 = 0
            for x in range(0, len(split1), 2):
                acc2 += eval(split1[x]) * eval(split1[x+1])
            acc2 = round(acc2 / 100, 1)
            class_average += acc2
            out_file.write(split[0] + "'s average: ")
            out_file.write(str(acc2) + "\n")
    class_average = round(class_average / acc, 1)
    out_file.write("Class average: " + str(class_average))
    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()