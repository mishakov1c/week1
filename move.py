from board import print_board
from checkings import check_draw, check_endgame
from config import CELLS
from constants import EMPTY_BLOCK, CPU_NAME
from random import randint
from typing import Tuple, Union


class MoveResult():
    def __init__(self, endgame, is_draw):
        self.endgame = endgame
        self.is_draw = is_draw


def bot_move() -> Tuple[int, int]:
    position = (randint(0, CELLS - 1), randint(0, CELLS - 1))
    while not move_is_correct(position):
        position = (randint(0, CELLS - 1), randint(0, CELLS - 1))    
    print(f'cpu делает ход {position}')
    
    return position


def players_move(player: str) -> Tuple[int, int]:
    raw_move = input(f'{player}, сделайте ход.\n')

    while not raw_move.isnumeric() and not move_is_correct(raw_move):
        raw_move = input(f'{player}, сделайте корректный ход (2 цифры).\n')    

    move = (int(raw_move[0]), int(raw_move[1]))

    return move


def move_is_correct(move: Union[str, Tuple[int, int]]) -> bool: 
    return (len(move) == 2) and (int(move[0]) <= (CELLS - 1)
        and int(move[1]) <= (CELLS - 1))


def make_move(gameboard: list, current_player: str, current_mark: str, is_endgame: bool, is_draw: bool) -> MoveResult:
    row, column = move_position(current_player)
    
    while gameboard[row][column] != EMPTY_BLOCK:
        print(f'Клетка {row}{column} занята, выберите другую.')
        row, column = move_position(current_player)
    
    gameboard[row][column] = current_mark
    
    print_board(gameboard)
        
    is_endgame = check_endgame(gameboard)

    if is_endgame:
        winner = current_player
        print(f'Победил {winner}')

    is_draw = check_draw(gameboard)

    if is_draw:
        print('Ничья')

    return MoveResult(endgame=is_endgame, is_draw=is_draw)
 

def move_position(current_player: str) -> Tuple[int, int]:
    position = bot_move() if current_player == CPU_NAME else players_move(current_player)
    return position


def get_current_player(player_name):
    player_plays_first = randint(0, 1)
    
    if player_plays_first:
        current_player = player_name
    else:
        current_player = CPU_NAME
    return current_player
