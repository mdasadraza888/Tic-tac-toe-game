#step - 1
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    