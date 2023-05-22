from config import COLUMNS, ROWS, EMPTY_BLOCK


def board() -> list:
    board = []

    for _ in range(ROWS):
        row = [EMPTY_BLOCK] * COLUMNS
        board.append(row)

    return board


def print_board(board: list) -> None:
    for row in range(ROWS):
        for col in range(COLUMNS):
            block_value = board[col][row]
            print(block_value, end=' ')
            if col < COLUMNS - 1:
                print('|', end=' ')
        print()
        if row < ROWS - 1:
            print('- ' * (COLUMNS * 2 - 1))
