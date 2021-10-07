"""
Jonathan Neideigh

greeting.py

This program displays a greeting card

I hereby certify that this assignment is entirely my work

"""

import time
from graphics import GraphWin, Circle, Point, Polygon, Text, Line

def greeting_card():
    width = 500
    height = 500
    win = GraphWin("Greeting Card", width, height)
    win.setCoords(0,0,20,20)

    ap1 = Point(-22, -22)
    ap2 = Point(-10, -10)
    line = Line(ap1, ap2)
    line.setFill("red")
    line.setOutline("red")

    ah1 = Point(-10,-10)
    ah2 = Point(-11,-10)
    ahl1 = Line(ah1,ah2)
    ahl1.setFill("red")
    ahl1.setOutline("red")

    ah3 = Point(-10,-10)
    ah4 = Point(-10,-11)
    ahl2 = Line(ah3,ah4)
    ahl2.setFill("red")
    ahl2.setOutline("red")

    ah5 = Point(-22,-22)
    ah6 = Point(-23,-22)
    ahl3 = Line(ah5,ah6)
    ahl3.setFill("red")
    ahl3.setOutline("red")

    ah7 = Point(-22,-22)
    ah8 = Point(-22,-23)
    ahl4 = Line(ah7,ah8)
    ahl4.setFill("red")
    ahl4.setOutline("red")

    ah9 = Point(-21,-21)
    ah10 = Point(-22, -21)
    ahl5 = Line(ah9,ah10)
    ahl5.setFill("red")
    ahl5.setOutline("red")

    ah11 = Point(-21,-21)
    ah12 = Point(-21,-22)
    ahl6 = Line(ah11,ah12)
    ahl6.setFill("red")
    ahl6.setOutline("red")

    point1 = Point(12,12)
    point2 = Point(7,12)
    heart = Circle(point1, 3)
    heart.setOutline("pink")
    heart.setFill("pink")

    point3 = Point(4.133,11)
    point4 = Point(10,11)
    point5 = Point(14.85,11)
    point6 = Point(10, 3)

    poly = Polygon(point3,point4,point5,point6)
    poly.setOutline("pink")
    poly.setFill("pink")

    heart2 = Circle(point2, 3)
    heart2.setOutline("pink")
    heart2.setFill("pink")

    line.draw(win)
    ahl1.draw(win)
    ahl2.draw(win)
    ahl3.draw(win)
    ahl4.draw(win)
    ahl5.draw(win)
    ahl6.draw(win)
    heart.draw(win)
    heart2.draw(win)
    poly.draw(win)


    inst_point = Point(10,12)
    inst_point2 = Point(10,10)
    inst_point3 = Point(10, 8)
    instructions = Text(inst_point, "Happy")
    instructions2 = Text(inst_point2, "Valentine's")
    instructions3 = Text(inst_point3, "Day!")
    instructions.draw(win)
    instructions.setFill("blue")
    instructions.setOutline("blue")
    instructions2.draw(win)
    instructions2.setFill("blue")
    instructions2.setOutline("blue")
    instructions3.draw(win)
    instructions3.setFill("blue")
    instructions3.setOutline("blue")

    for i in range(1,14):
        line.move(2,2)
        ahl1.move(2,2)
        ahl2.move(2,2)
        ahl3.move(2,2)
        ahl4.move(2,2)
        ahl5.move(2,2)
        ahl6.move(2,2)
        time.sleep(.1)

    inst_pt = Point(10, 1)
    instructions4 = Text(inst_pt, "Click again to close")
    instructions4.draw(win)

    win.getMouse()
    win.close()


greeting_card()
