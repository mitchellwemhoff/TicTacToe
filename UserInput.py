class UserInput:

    def get_input_for_move(self):
        y = input('What is the Y coordinate of your move:\n')
        x = input('What is the X coordinate of your move:\n')
        return str([y,x]).replace(" ", "").replace("'", "")

    def is_human_first_player(self):
        is_human_first_player = input('Do you wish to go first? (y/n)')
        if is_human_first_player == 'y':
            return True
        else:
            return False