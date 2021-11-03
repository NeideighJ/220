"""
Name: Jonathan Neideigh
lab10.py
"""

def build():
    return list(range(1,10))

def display(board):
    for i in range(3):
        n = i * 3
        print(board[n], '|' , board[n+1] , '|',  board[n+2])
        print(10 * "-")

def place(board,pos,piece):
    if piece == "x" or "o":
        board[pos-1] = piece

def legal(board,pos):
    if board[pos-1]==pos:
        return True
    return False

def isWon(board,piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3]!=piece:
            continue
        if board[i+6]!=piece:
            continue
        return True
    if board[0]==piece:
        if board[4]==piece:
            if board[8]==piece:
                return True
    if board[2]==piece:
        if board[4]==piece:
            if board[6]==piece:
                return True
    return False


def over(board):
    if isWon(board,"X"):
        return True
    elif isWon(board, "O"):
        return True
    else:
        for i in range(9):
            if board[i]==i+1:
                return False
        return True

def play():
    create_board = build()
    while True:
        display(create_board)
        x_move = eval(input("Where does player X want to put their piece?: "))
        while not legal(create_board,x_move):
            x_move = eval(input("Where does player X want to put their piece?: "))
        place(create_board,x_move,"X")
        if over(create_board):
            if isWon(create_board,"X"):
                display(create_board)
                print("Player X wins!")
                exit()
            if isWon(create_board,"O"):
                display(create_board)
                print("Player O wins!")
                exit()
            print("It's a tie!")
        display(create_board)
        o_move = eval(input("Where does player O want to put their piece?: "))
        while not legal(create_board,o_move):
            o_move = eval(input("Where does player O want to put their piece?: "))
        place(create_board,o_move,"O")
        if over(create_board):
            if isWon(create_board,"O"):
                display(create_board)
                print("Player O wins!")
                exit()
            if isWon(create_board,"X"):
                display(create_board)
                print("Player X wins!")
                exit()
            print("It's a tie!")
            break


def main():
    play()
    pass


main()
