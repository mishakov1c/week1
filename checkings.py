from config import COLUMNS, ROWS, EMPTY_BLOCK


def check_endgame(board):
    for row in range(ROWS):
        if all(board[f'0{row}'] == board[f'{col}{row}'] != EMPTY_BLOCK for col in range(COLUMNS)):            
            return True
        
    for col in range(COLUMNS):
        if all(board[f'{col}0'] == board[f'{col}{row}'] != EMPTY_BLOCK for row in range(ROWS)):
            return True
        
    if all(board['00'] == board[f'{i}{i}'] != EMPTY_BLOCK for i in range(ROWS)):
        return True

    if all(board[f'0{ROWS - 1}'] == board[f'{i}{ROWS - i - 1}'] != EMPTY_BLOCK for i in range(ROWS)):
        return True

    return False   


def check_draw(board):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[f'{col}{row}'] == EMPTY_BLOCK:
                return False
            
    return True