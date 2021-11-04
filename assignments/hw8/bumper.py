"""
Jonathan Neideigh

bumper.py

This assignment simulates a bumper car amusement park ride

I hereby certify that this assignment is entirely my work
"""
import math
from random import randint
import time
from graphics import GraphWin, Circle, Point, color_rgb



def main():
    width = 500
    height = 500
    win = GraphWin("Bumper", width, height)
    color1 = get_random_color()
    color2 = get_random_color()

    point1 = Point(100,100)
    radius = 20
    circle1 = Circle(point1,radius)
    circle1.setFill(color1)
    circle1.setOutline(color1)
    circle1.draw(win)

    point2 = Point(300,300)
    circle2 = Circle(point2,radius)
    circle2.setFill(color2)
    circle2.setOutline(color2)
    circle2.draw(win)

    bump_move(circle1,circle2,win)


def bump_move(circle1,circle2,win):
    dx1 = get_random(5)
    dy1 = get_random(5)
    dx2 = get_random(8)
    dy2 = get_random(6)
    while 100 > 0:
        circle1.move(dx1,dy1)
        circle2.move(dx2,dy2)
        if hit_horizontal(circle1,win):
            dy1 = -dy1
        if hit_vertical(circle1,win):
            dx1 = -dx1
        if hit_horizontal(circle2,win):
            dy2 = -dy2
        if hit_vertical(circle2,win):
            dx2 = -dx2
        if did_collide(circle1,circle2):
            dx1 = -dx1
            dy1 = -dy1
            dx2 = -dx2
            dy2 = -dy2
        time.sleep(.01)


def get_random(move_amount):
    return randint(-move_amount,move_amount)


def did_collide(circle1, circle2):
    center1 =  circle1.getCenter()
    center2 = circle2.getCenter()
    radius1 = circle1.getRadius()
    radius2 = circle2.getRadius()
    circle1x = center1.getX()
    circle1y = center1.getY()
    circle2x = center2.getX()
    circle2y = center2.getY()
    distance = math.sqrt(((circle2x-circle1x)**2)+((circle2y-circle1y)**2))
    if distance <= (radius1+radius2):
        return True
    return False


def hit_horizontal(circle1,win):
    circle1_center = circle1.getCenter()
    circle1_y = circle1_center.getY()
    radius = circle1.getRadius()
    height_low = radius
    height_high = win.getHeight()-radius
    return circle1_y <= height_low or circle1_y >= height_high


def hit_vertical(circle1,win):
    circle1_center = circle1.getCenter()
    circle1_x = circle1_center.getX()
    radius = circle1.getRadius()
    width_low = radius
    width_high = win.getWidth() - radius
    return circle1_x <= width_low or circle1_x >= width_high


def get_random_color():
    red = randint(0,256)
    blue = randint(0,256)
    green = randint(0,256)
    return color_rgb(red,green,blue)

if __name__ == '__main__':
    main()
