class AI:
    def calculate_move_idiot(self, board):
        if board.board_str[1] not in ['X', 'O']:
            return '[3,1]'
        if board.board_str[5] not in ['X', 'O']:
            return '[3,2]'
        if board.board_str[9] not in ['X', 'O']:
            return '[3,3]'
        if board.board_str[13] not in ['X', 'O']:
            return '[2,1]'
        if board.board_str[17] not in ['X', 'O']:
            return '[2,2]'
        if board.board_str[21] not in ['X', 'O']:
            return '[2,3]'
        if board.board_str[25] not in ['X', 'O']:
            return '[1,1]'
        if board.board_str[29] not in ['X', 'O']:
            return '[1,2]'
        if board.board_str[33] not in ['X', 'O']:
            return '[1,3]'
