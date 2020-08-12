class UserInput:

    def validate_coordinate(self, coordinate):
        if coordinate in ['1','2','3']:
            return True
        return False

    def get_input_for_move(self):
        y = input('What is the Y coordinate of your move:\n')
        while not self.validate_coordinate(y):
            print("Invalid Coordinate")
            y = input('What is the Y coordinate of your move:\n')
        x = input('What is the X coordinate of your move:\n')
        while not self.validate_coordinate(x):
            print("Invalid Coordinate")
            y = input('What is the Y coordinate of your move:\n')
        return str([y,x]).replace(" ", "").replace("'", "")

    def is_human_first_player(self):
        is_human_first_player = input('Do you wish to go first? (y/n)')
        if is_human_first_player == 'y':
            return True
        else:
            return False
