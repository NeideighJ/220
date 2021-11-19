from random import shuffle
from graphics import GraphWin, Point, Text
from button import Button


def main():
    win = GraphWin('Three Door Game', 500, 500)
    win.setCoords(0, 0, 600, 600)

    door1 = Button(Point(125, 300), 70, 60, 'Door 1')
    door1.draw(win)
    door2 = Button(Point(300, 300), 70, 60, 'Door 2')
    door2.draw(win)
    door3 = Button(Point(475, 300), 70, 60, 'Door 3')
    door3.draw(win)
    secret_door_text = Text(Point(300, 500), 'I have a secret door')
    secret_door_text.draw(win)
    secret_text = Text(Point(300, 100), 'Click to choose my door')
    secret_text.draw(win)
    mouse_click = win.getMouse()
    secret_list = [0, 0, 1]
    secret_value = 1
    shuffle(secret_list)
    door1_value = secret_list[0]
    door2_value = secret_list[1]
    door3_value = secret_list[2]

    if door1.is_clicked(mouse_click) and door1_value == secret_value:
        door1.color_button('green')
        secret_door_text.setText('You Win!')
        secret_text.setText('Click to close')
    elif door1.is_clicked(mouse_click) and door1_value != secret_value:
        door1.color_button('red')
        secret_door_text.setText('You Lost!')
        if door2_value == secret_value:
            secret_text.setText('Door 2 is my secret door')
        elif door3_value == secret_value:
            secret_text.setText('Door 3 is my secret door')
    elif door2.is_clicked(mouse_click) and door2_value == secret_value:
        door2.color_button('green')
        secret_door_text.setText('You Win!')
        secret_text.setText('Click to close')
    elif door2.is_clicked(mouse_click) and door2_value != secret_value:
        door2.color_button('red')
        secret_door_text.setText('You Lost!')
        if door1_value == secret_value:
            secret_text.setText('Door 1 is my secret door')
        elif door3_value == secret_value:
            secret_text.setText('Door 3 is my secret door')
    elif door3.is_clicked(mouse_click) and door3_value == secret_value:
        door3.color_button('green')
        secret_door_text.setText('You Win!')
        secret_text.setText('Click to close')
    elif door3.is_clicked(mouse_click) and door3_value != secret_value:
        door3.color_button('red')
        secret_door_text.setText('You Lost!')
        if door2_value == secret_value:
            secret_text.setText('Door 2 is my secret door')
        elif door1_value == secret_value:
            secret_text.setText('Door 1 is my secret door')

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
