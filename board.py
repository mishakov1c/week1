from config import CELLS
from constants import EMPTY_BLOCK

def board() -> list[list[str]]:
    board = []

    for _ in range(CELLS):
        row = [EMPTY_BLOCK] * CELLS
        board.append(row)

    return board


def print_board(board: list) -> None:
    for row in range(CELLS):
        for col in range(CELLS):
            block_value = board[row][col]
            print(block_value, end=' ')
            if col < CELLS - 1:
                print('|', end=' ')
        print()
        if row < CELLS - 1:
            print('- ' * (CELLS * 2 - 1))
