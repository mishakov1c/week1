from config import COLUMNS, ROWS, EMPTY_BLOCK


def board():
    board = {}

    for row in range(ROWS):
        for column in range(COLUMNS):
            position = f'{column}{row}'
            board[position] = EMPTY_BLOCK

    return board


def print_board(board):
    for row in range(ROWS):
        for col in range(COLUMNS):
            block_value = board[f'{col}{row}']
            print(block_value, end=' ')
            if col < COLUMNS - 1:
                print('|', end=' ')
        print()
        if row < ROWS - 1:
            print('- ' * (COLUMNS * 2 - 1))