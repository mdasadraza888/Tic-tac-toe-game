#step - 9
def replay():
    playing = None

    while playing not in ['yes', 'no']:
        playing = input("Would you like to play the game again 'yes' or 'no': ")

    if playing == 'yes':
        return True
    else:
        return False