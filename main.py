from Board import Board
from AI import AI
from UserInput import UserInput

board = Board()
ai = AI()
user_input = UserInput()

def human_goes_first(board):
    while True:
        human_move = user_input.get_input_for_move()
        human_is_valid_move, is_game_over, is_cats_game = board.input_move(human_move)
        while not human_is_valid_move:
            print("Invalid move")
            human_move = user_input.get_input_for_move()
            human_is_valid_move, is_game_ove, is_cats_game = board.input_move(human_move)
        print(board.board_str)
        if is_game_over:
            print("Game Over")
        if is_cats_game:
            print("Cat's Game")
            break

        print('AI is thinking...')
        ai_move = ai.calculate_move_genius(board)
        ai_is_valid_move, is_game_over, is_cats_game = board.input_move(ai_move)
        print(board.board_str)
        if is_game_over:
            print("Game Over")
        if is_cats_game:
            print("Cat's Game")
            break

def ai_goes_first(board):
    while True:
        print('AI is thinking...')
        ai_move = ai.calculate_move_genius(board)
        ai_is_valid_move, is_game_over, is_cats_game = board.input_move(ai_move)
        print(board.board_str)
        if is_game_over:
            print("Game Over")
        if is_cats_game:
            print("Cat's Game")
            break

        human_move = user_input.get_input_for_move()
        human_is_valid_move, is_game_over, is_cats_game = board.input_move(human_move)
        while not human_is_valid_move:
            print("Invalid move")
            human_move = user_input.get_input_for_move()
            human_is_valid_move, is_game_over, is_cats_game = board.input_move(human_move)
        print(board.board_str)
        if is_game_over:
            print("Game Over")
        if is_cats_game:
            print("Cat's Game")
            break

if __name__ == '__main__':
    is_human_first_player = user_input.is_human_first_player()

    if is_human_first_player:
        human_goes_first(board)
    else:
        ai_goes_first(board)
