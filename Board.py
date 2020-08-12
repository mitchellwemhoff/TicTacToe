class Board:
    board_str = '''___|___|___\n___|___|___\n   |   |   '''

    coordinate_dict = {
        '[1,1]': 25,
        '[1,2]': 29,
        '[1,3]': 33,
        '[2,1]': 13,
        '[2,2]': 17,
        '[2,3]': 21,
        '[3,1]': 1,
        '[3,2]': 5,
        '[3,3]': 9
    }

    players = {
        -1: 'X',
        1: 'O'
    }

    current_player_index = -1

    def __init__(self):
        pass

    def input_move(self, coordinate):
        is_valid_move = self.validate_move(self.coordinate_dict[coordinate])
        if is_valid_move:
            self.board_str = self.place_move(coordinate, self.players[self.current_player_index], self.board_str)
            self.current_player_index *= -1
        is_game_over = self.get_game_over(self.board_str)
        return is_valid_move, is_game_over

    def place_move(self, coordinate, player, board):
        return self.populate(board, self.coordinate_dict[coordinate], player)

    def populate(self, board, index, player):
        return board[:index] + player + board[index + 1:]

    def validate_move(self, index):
        if self.board_str[index] != 'X' and self.board_str[index] != 'O':
            return True
        return False

    def game_over(self, board):
        if board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
            return True
        elif board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
            return True
        if board[13] == 'X' and board[17] == 'X' and board[21] == 'X':
            return True
        elif board[13] == 'O' and board[17] == 'O' and board[21] == 'O':
            return True
        if board[25] == 'X' and board[29] == 'X' and board[33] == 'X':
            return True
        elif board[25] == 'O' and board[29] == 'O' and board[33] == 'O':
            return True
        if board[1] == 'X' and board[13] == 'X' and board[25] == 'X':
            return True
        elif board[1] == 'O' and board[13] == 'O' and board[25] == 'O':
            return True
        if board[5] == 'X' and board[17] == 'X' and board[29] == 'X':
            return True
        elif board[5] == 'O' and board[17] == 'O' and board[29] == 'O':
            return True
        if board[9] == 'X' and board[21] == 'X' and board[33] == 'X':
            return True
        elif board[9] == 'O' and board[21] == 'O' and board[33] == 'O':
            return True
        if board[1] == 'X' and board[17] == 'X' and board[33] == 'X':
            return True
        elif board[1] == 'O' and board[17] == 'O' and board[33] == 'O':
            return True
        if board[9] == 'X' and board[17] == 'X' and board[25] == 'X':
            return True
        elif board[9] == 'O' and board[17] == 'O' and board[25] == 'O':
            return True
        return False

    def full_board(self, board):
        if board[1] in ['X', 'O'] and board[5] in ['X', 'O'] and board[9] in \
            ['X', 'O'] and board[13] in ['X', 'O'] and board[17] in ['X', 'O'] and \
            board[21] in ['X', 'O'] and board[25] in ['X', 'O'] and board[29] in \
            ['X', 'O'] and board[33] in ['X', 'O']:
            return True
        return False

    def get_game_over(self, board):
        return_boolean = self.game_over(board) or self.full_board(board)
        return return_boolean