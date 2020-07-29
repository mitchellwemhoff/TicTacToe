#board
emptyBoard = '''___|___|___\n___|___|___\n   |   |   '''

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

def move(coordinate, player, board):
    if coordinate == [1,1]:
        board = place_move(25, player, board)
    elif coordinate == [1,2]:
        board = place_move(29, player, board)
    elif coordinate == [1,3]:
        board = place_move(33, player, board)
    elif coordinate == [2,1]:
        board = place_move(13, player, board)
    elif coordinate == [2,2]:
        board = place_move(17, player, board)
    elif coordinate == [2,3]:
        board = place_move(21, player, board)
    elif coordinate == [3,1]:
        board = place_move(1, player, board)
    elif coordinate == [3,2]:
        board = place_move(5, player, board)
    elif coordinate == [3,3]:
        board = place_move(9, player, board)
    return board

def place_move(index, player, board):
    while True:
        if validate_move(index, player, board):
            board = board[:index] + player + board[index + 1:]
            break
        else:
            print('Duplicate Move')
            index = coordinate_dict[str(get_input_for_move()).replace(" ", "")]
    return board

def validate_move(index, player, board):
    if board[index] != 'X' and board[index] != 'O':
        return True
    return False

def validate_coordinate(coordinate):
    if coordinate in ['1','2','3']:
        return True
    return False

def get_input_for_move():
    y = input('What is the Y coordinate of your move:\n')
    if validate_coordinate(y):
        y = int(y)
    else:
        while True:
            print('not a valid move')
            y = input('What is the Y coordinate of your move:\n')
            if validate_coordinate(y):
                y = int(y)
                break
    x = input('What is the X coordinate of your move:\n')
    if validate_coordinate(x):
        x = int(x)
    else:
        while True:
            print('not a valid move')
            x = input('What is the X coordinate of your move:\n')
            if validate_coordinate(x):
                x = int(x)
                break
    return [y, x]

def game_over(board):
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

def full_board(board):
    if board[1] in ['X', 'O'] and board[5] in ['X', 'O'] and board[9] in \
        ['X', 'O'] and board[13] in ['X', 'O'] and board[17] in ['X', 'O'] and \
        board[21] in ['X', 'O'] and board[25] in ['X', 'O'] and board[29] in \
        ['X', 'O'] and board[33] in ['X', 'O']:
        return True
    return False

def play():
    board = move(get_input_for_move(), 'O', emptyBoard)
    print(board)
    board = move(get_input_for_move(), 'X', board)
    print(board)
    if game_over(board):
        print('game over')
    else:
        while True:
            board = move(get_input_for_move(), 'O', board)
            print(board)
            if game_over(board):
                print('game over')
                break
            if full_board(board):
                print('cats game')
                break
            board = move(get_input_for_move(), 'X', board)
            print(board)
            if game_over(board):
                print('game over')
                break
            if full_board(board):
                print('''cat's game''')
                break
