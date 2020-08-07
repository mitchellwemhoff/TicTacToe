import GameLogic
from Board import Board

board = Board()
is_valid_move, is_game_over = board.input_move('[2,2]')
is_valid_move, is_game_over = board.input_move('[1,2]')
print()

# from Car import Car
#
# car1 = Car(4, 'Chevrolet')
# print(car1.amount_of_gas)
# car1.add_gas(10)
#
# print(car1.brand)
# print(car1.wheels)
# print(car1.amount_of_gas)