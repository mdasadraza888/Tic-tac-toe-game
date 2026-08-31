from choose_player_first import choose_first
from display import display_board
from full_board_check import full_board_check
from place_marker import place_marker
from player_choice import player_choice
from player_input import player_input
from replay import replay
from space_check import space_check
from win_check import win_check


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' '] * 10
    board[0] = '#'
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    
    play_game = input("Are you ready to play the game? Enter Yes or No: ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        #Player 1 Turn
        if turn == 'player1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                display_board(board)
                print("Congratulation, player1 has won the game.")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is draw.")
                    break
                else:
                    turn = 'player2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                display_board(board)
                print("Congratulation, player2 has won the game.")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is draw.")
                    break
                else:
                    turn = 'player1'
    if not replay():
        break