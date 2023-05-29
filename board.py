from config import NUM_OF_CELLS
from enums import TicTacToeSymbol


def board() -> list[list[str]]:
    return [[TicTacToeSymbol.EMPTY.value] * NUM_OF_CELLS for _ in range(NUM_OF_CELLS)]


def print_board(board: list[list[str]]) -> None:
    for row in board:
        for col, block_value in enumerate(row):
            print(block_value, end=" ")
            if col < NUM_OF_CELLS - 1:
                print("|", end=" ")
        print()
        if row is not board[-1]:
            print("- " * (NUM_OF_CELLS * 2 - 1))
