"""
Jonathan Neideigh

traffic.py

This program analyzes traffic patterns

I certify that this assignment is entirely my work
"""

def main():

    num_roads = eval(input("How many roads were surveyed? "))
    total_vehicles = 0
    for i in range(num_roads):
        days = eval(input("How many days was road " + str(i + 1 ) + " surveyed ? "))
        acc = 0
        for j in range(days):
            cars = eval(input("How many cars traveled on day " + str(j + 1) + " ? "))
            acc = acc + cars
            total_vehicles = total_vehicles + cars
            average = acc / days
        print("Road " + str(i + 1) + " average vehicles per day : ", round(average, 2))
    average_cars = total_vehicles / num_roads
    print("Total number of vehicles traveled on all roads: ", str(total_vehicles))
    print("Average number of vehicles per road: " , round(average_cars, 2))


if __name__ == '__main__':
    main()
