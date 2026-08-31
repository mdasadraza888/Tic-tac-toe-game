#step -2
from IPython.display import clear_output

def player_input():
    marker = ''
    
    while marker not in ['X', 'O']:
        marker = input("Player1: Enter your marker ('x', 'o'): ").upper()
        if marker not in ['X', 'O']:
            clear_output()
            print("This is not valid marker please try to mark right marker:")
            
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
