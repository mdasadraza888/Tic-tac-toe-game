#step - 8
from space_check import space_check

def player_choice(board):
    position = None
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Enter position 1 to 9 to mark your marker: "))

    return position