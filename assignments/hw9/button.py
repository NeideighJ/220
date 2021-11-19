"""
Jonathan Neideigh

three_door_game.py

I hereby certify that this assignment is entirely my work

"""


from graphics import Point, Rectangle, Text


class Button:

    def __init__(self, center, width, height, label):
        x = center.getX()
        y = center.getY()
        self.x_min = x - width
        self.x_max = x + width
        self.y_min = y - height
        self.y_max = y + height
        p1 = Point(self.x_min, self.y_min)
        p2 = Point(self.x_max, self.y_max)
        self.shape = Rectangle(p1, p2)
        self.label = Text(center, label)

    def get_label(self):
        return self.label.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.label.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.label.undraw()

    def is_clicked(self, point):
        return self.x_min <= point.getX() <= self.x_max and \
               self.y_min <= point.getY() <= self.y_max

    def color_button(self, color):
        self.shape.setFill(color)
        self.shape.setOutline(color)

    def set_label(self, label):
        self.label = label.setText()
