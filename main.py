import GameLogic
import Board

emptyBoard_str = '''___|___|___\n___|___|___\n   |   |   '''

board = Board
board = board.input_move('[2,2]', 'O', emptyBoard_str)
board = board.input_move('[1,2]', 'X', board)
print()