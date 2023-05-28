from config import CELLS
from constants import EMPTY_BLOCK 

def check_endgame(board: list) -> bool:
    for row in range(CELLS):
        if all(board[row][0] == board[row][col] != EMPTY_BLOCK for col in range(CELLS)):            
            return True
        
    for col in range(CELLS):
        if all(board[0][col] == board[row][col] != EMPTY_BLOCK for row in range(CELLS)):
            return True
        
    if all(board[0][0] == board[i][i] != EMPTY_BLOCK for i in range(CELLS)):
        return True

    if all(board[CELLS - 1][0] == board[CELLS - i - 1][i] != EMPTY_BLOCK for i in range(CELLS)):
        return True

    return False  


def check_draw(board: list) -> bool:
    for row in range(CELLS):
        for col in range(CELLS):
            if board[row][col] == EMPTY_BLOCK:
                return False
            
    return True
