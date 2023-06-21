from config import NUM_OF_CELLS
from enums import TicTacToeSymbol


def check_endgame(board: list[list[TicTacToeSymbol]]) -> bool:
    for row in range(NUM_OF_CELLS):
        if all(
            board[row][0] == board[row][col] != TicTacToeSymbol.EMPTY
            for col in range(NUM_OF_CELLS)
        ):
            return True

    for col in range(NUM_OF_CELLS):
        if all(
            board[0][col] == board[row][col] != TicTacToeSymbol.EMPTY
            for row in range(NUM_OF_CELLS)
        ):
            return True

    if all(
        board[0][0] == board[i][i] != TicTacToeSymbol.EMPTY
        for i in range(NUM_OF_CELLS)
    ):
        return True

    if all(
        board[NUM_OF_CELLS - 1][0] == board[NUM_OF_CELLS - i - 1][i] != TicTacToeSymbol.EMPTY
        for i in range(NUM_OF_CELLS)
    ):
        return True

    return False


def check_draw(board: list[list[TicTacToeSymbol]]) -> bool:
    for row in range(NUM_OF_CELLS):
        for col in range(NUM_OF_CELLS):
            if board[row][col] == TicTacToeSymbol.EMPTY:
                return False
    return True
