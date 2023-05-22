from board import print_board
from checkings import check_draw, check_endgame
from config import COLUMNS, ROWS, EMPTY_BLOCK, O_MARK, X_MARK
from random import randint


class MoveResult():
    def __init__(self, endgame, is_draw):
        self.endgame = endgame
        self.is_draw = is_draw


def bot_move() -> str:
    position = f'{randint(0, COLUMNS - 1)}{randint(0, ROWS - 1)}'
    print(f'cpu делает ход {position}')
    
    return position


def players_move(player: str) -> str:
    move = input(f'{player}, сделайте ход.\n')
    while move_is_not_correct(move):
        move = input(f'{player}, сделайте корректный ход (2 цифры).\n')    

    return move


def move_is_not_correct(move: str) -> bool:
    return ((len(move) != 2) or (not move.isnumeric())
        or (int(move[0]) > (ROWS - 1) or int(move[1]) > (COLUMNS - 1)))


def make_move(gameboard: list, queue: dict[str, str], player_name: str, is_endgame: bool, is_draw: bool) -> MoveResult:
    for k, v in queue.items():
        column, row = move_position(player_name, v)
        
        while gameboard[column][row] != EMPTY_BLOCK:
            print(f'Клетка {column}{row} занята, выберите другую.')
            column, row = move_position(player_name, v)
        
        gameboard[column][row] = k
        
        print_board(gameboard)
            
        is_endgame = check_endgame(gameboard)

        if is_endgame:
            winner = queue[k]
            print(f'Победил {winner}')
            break

        is_draw = check_draw(gameboard)

        if is_draw:
            print('Ничья')
            break

    return MoveResult(endgame=is_endgame, is_draw=is_draw)
 

def move_position(player_name: str, current_player: str) -> tuple[int, int]:
    raw_position = players_move(current_player) if current_player == player_name else bot_move()
    position = (int(raw_position[0]), int(raw_position[1]))
    return position


def queue_of_players(player_name: str, cpu_name: str) -> dict:
    player_plays_first = randint(0, 1)
    
    if player_plays_first:
        queue = {X_MARK: player_name, O_MARK: cpu_name}
    else:
        queue = {X_MARK: cpu_name, O_MARK: player_name}

    print(f'Первым ходит {queue[X_MARK]}.')
    return queue
