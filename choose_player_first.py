# step - 5
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'player2'
    else:
        return 'player1'