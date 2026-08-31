#step - 7
from space_check import space_check

def full_board_check(board):
    for i in range(len(board)):
        if space_check(board, i):
            return False

    return True