from config import COLUMNS, ROWS, EMPTY_BLOCK
 

def check_endgame(board: list) -> bool:
    for row in range(ROWS):
        if all(board[0][row] == board[col][row] != EMPTY_BLOCK for col in range(COLUMNS)):            
            return True
        
    for col in range(COLUMNS):
        if all(board[col][0] == board[col][row] != EMPTY_BLOCK for row in range(ROWS)):
            return True
        
    if all(board[0][0] == board[i][i] != EMPTY_BLOCK for i in range(ROWS)):
        return True

    if all(board[0][ROWS - 1] == board[i][ROWS - i - 1] != EMPTY_BLOCK for i in range(ROWS)):
        return True

    return False  


def check_draw(board: list) -> bool:
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[col][row] == EMPTY_BLOCK:
                return False
            
    return True
