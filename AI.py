import random

class AI:

    player  = ''

    other_player = ''

    coordinate_dict = {
        25: '[1,1]',
        29: '[1,2]',
        33: '[1,3]',
        13: '[2,1]',
        17: '[2,2]',
        21: '[2,3]',
        1: '[3,1]',
        5: '[3,2]',
        9: '[3,3]'
    }

    winning_lanes = [
        [25, 29, 33],
        [13, 17, 21],
        [1, 5, 9],
        [25, 13, 1],
        [29, 17, 5],
        [33, 21, 9],
        [25, 17, 9],
        [33, 17, 1]
    ]

    # def calculate_move_idiot(self, board):
    #     if board.board_str[1] not in ['X', 'O']:
    #         return '[3,1]'
    #     if board.board_str[5] not in ['X', 'O']:
    #         return '[3,2]'
    #     if board.board_str[9] not in ['X', 'O']:
    #         return '[3,3]'
    #     if board.board_str[13] not in ['X', 'O']:
    #         return '[2,1]'
    #     if board.board_str[17] not in ['X', 'O']:
    #         return '[2,2]'
    #     if board.board_str[21] not in ['X', 'O']:
    #         return '[2,3]'
    #     if board.board_str[25] not in ['X', 'O']:
    #         return '[1,1]'
    #     if board.board_str[29] not in ['X', 'O']:
    #         return '[1,2]'
    #     if board.board_str[33] not in ['X', 'O']:
    #         return '[1,3]'

    def calculate_move_genius(self, board):
        if self.get_number_of_moves(board) == 0:
            self.player = 'X'
            self.other_player = 'O'
            return self.first_move_play_center_move_one()
        if self.get_number_of_moves(board) == 1:
            self.player = 'O'
            self.other_player = 'X'
            return self.first_move_move_two(board)
        return self.middle_moves(board)

    def extract_moves_from_board(self, board):
        moves_dict = dict()
        postions_on_board = [1, 5, 9, 13, 17, 21, 25, 29, 33]
        for position in postions_on_board:
            if board.board_str[position] == 'X':
                try:
                    existing_moves = moves_dict['X']
                    existing_moves.append(position)
                except:
                    moves = [position]
                    moves_dict['X'] = moves
            if board.board_str[position] == 'O':
                try:
                    existing_moves = moves_dict['O']
                    existing_moves.append(position)
                except:
                    moves = [position]
                    moves_dict['O'] = moves
        return moves_dict

    def first_move_play_center_move_one(self):
        return '[2,2]'

    def first_move_move_two(self, board):
        if board.board_str[17] not in ['X', 'O']:
            return '[2,2]'
        if board.board_str[17] in ['X', 'O']:
            return random.sample(['[3,1]', '[3,3]', '[1,1]', '[1,3]'], 1)[0]

    def middle_moves(self, board):
        moves_dict = self.extract_moves_from_board(board)
        if self.moves_until_ai_wins(moves_dict) == 1:
            return self.play_offense(moves_dict)
        if self.moves_until_human_wins(moves_dict) == 1:
            return self.play_defense(moves_dict)
        return self.play_offense(moves_dict)

    def do_moves_exist_in_lane(self, moves, lane):
        for position in moves:
            if position in lane:
                return True
        return False

    def lane_move_counter(self, moves, lane):
        count = 0
        for position in lane:
            if position in moves:
                count += 1
        return count

    def moves_until_human_wins(self, moves_dict):
        ai_moves = moves_dict[self.player]
        human_moves = moves_dict[self.other_player]
        moves_until_human_wins = 3
        for lane in self.winning_lanes:
            human_moves_in_lane = 0
            if self.do_moves_exist_in_lane(human_moves, lane) and not self.do_moves_exist_in_lane(ai_moves, lane):
                for position in human_moves:
                    if position in lane:
                        human_moves_in_lane += 1
            if (3 - human_moves_in_lane) < moves_until_human_wins:
                moves_until_human_wins = 3 - human_moves_in_lane
        return moves_until_human_wins

    def moves_until_ai_wins(self, moves_dict):
        ai_moves = moves_dict[self.player]
        human_moves = moves_dict[self.other_player]
        moves_until_ai_wins = 3
        for lane in self.winning_lanes:
            ai_moves_in_lane = 0
            if self.do_moves_exist_in_lane(ai_moves, lane) and not self.do_moves_exist_in_lane(human_moves, lane):
                for position in ai_moves:
                    if position in lane:
                        ai_moves_in_lane += 1
            if (3 - ai_moves_in_lane) < moves_until_ai_wins:
                moves_until_ai_wins = 3 - ai_moves_in_lane
        return moves_until_ai_wins

    def play_offense(self, moves_dict):
        ai_moves = moves_dict[self.player]
        human_moves = moves_dict[self.other_player]
        if not self.moves_until_ai_wins(moves_dict) == 1:
            for lane in self.winning_lanes:
                if self.do_moves_exist_in_lane(ai_moves, lane) and not self.do_moves_exist_in_lane(human_moves, lane):
                    for position in lane:
                        if position not in ai_moves:
                            return self.coordinate_dict[position]
        if self.moves_until_ai_wins(moves_dict) == 1:
            for lane in self.winning_lanes:
                if self.do_moves_exist_in_lane(ai_moves, lane) and not self.do_moves_exist_in_lane(human_moves, lane) and self.lane_move_counter(ai_moves, lane) == 2:
                    for position in lane:
                        if position not in ai_moves:
                            return self.coordinate_dict[position]
        return self.call_it_quits(moves_dict)

    def call_it_quits(self, moves_dict):
        move_set = set()
        for player in moves_dict:
            for coordinate in moves_dict[player]:
                move_set.add(coordinate)
        total_moves_set = set(self.coordinate_dict.keys())
        last_move = total_moves_set - move_set
        return self.coordinate_dict[last_move.pop()]


    def play_defense(self, moves_dict):
        ai_moves = moves_dict[self.player]
        human_moves = moves_dict[self.other_player]
        for lane in self.winning_lanes:
            if not self.do_moves_exist_in_lane(ai_moves,lane) and self.do_moves_exist_in_lane(human_moves, lane):
                count = 0
                for position in lane:
                    if position in human_moves:
                        count += 1
                    if count == 2:
                        for space in lane:
                            if space not in human_moves:
                                return self.coordinate_dict[space]



    def get_number_of_moves(self, board):
        count = 0
        if board.board_str[1] in ['X', 'O']:
            count += 1
        if board.board_str[5] in ['X', 'O']:
            count += 1
        if board.board_str[9] in ['X', 'O']:
            count += 1
        if board.board_str[13] in ['X', 'O']:
            count += 1
        if board.board_str[17] in ['X', 'O']:
            count += 1
        if board.board_str[21] in ['X', 'O']:
            count += 1
        if board.board_str[25] in ['X', 'O']:
            count += 1
        if board.board_str[29] in ['X', 'O']:
            count += 1
        if board.board_str[33] in ['X', 'O']:
            count += 1
        return count
