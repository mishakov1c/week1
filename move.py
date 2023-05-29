from board import print_board
from checkings import check_draw, check_endgame
from config import NUM_OF_CELLS
from constants import CPU_NAME
from enums import TicTacToeSymbol
from random import randint
import dataclasses


@dataclasses.dataclass(kw_only=True, slots=True)
class MoveResult:
    is_endgame: bool
    is_draw: bool


def make_bot_move() -> tuple[int, int]:
    position = (randint(0, NUM_OF_CELLS - 1), randint(0, NUM_OF_CELLS - 1))
    while not move_is_correct(position):
        position = (randint(0, NUM_OF_CELLS - 1), randint(0, NUM_OF_CELLS - 1))    
    print(f'cpu делает ход {position}')
    
    return position


def make_players_move(player: str) -> tuple[int, int]:
    raw_move = input(f'{player}, сделайте ход.\n')

    while True:
        raw_move_is_numeric = raw_move.isnumeric() 
        if not raw_move_is_numeric or len(raw_move) != 2:
            raw_move = input(f'{player}, сделайте корректный ход (2 цифры).\n')
        else:
            move = (int(raw_move[0]), int(raw_move[1]))
            if move_is_correct(move):
                break

    return move


def move_is_correct(move: tuple[int, int]) -> bool: 
    return (
        (len(move) == 2)
        and (int(move[0]) <= (NUM_OF_CELLS - 1)
        and int(move[1]) <= (NUM_OF_CELLS - 1))
    )


def make_move(gameboard: list, current_player: str, current_mark: TicTacToeSymbol, is_endgame: bool, is_draw: bool) -> MoveResult:
    row, column = move_position(current_player)
    
    while gameboard[row][column] != TicTacToeSymbol.EMPTY.value:
        print(f'Клетка {row}{column} занята, выберите другую.')
        row, column = move_position(current_player)
    
    gameboard[row][column] = current_mark.value
    
    print_board(gameboard)
        
    is_endgame = check_endgame(gameboard)

    if is_endgame:
        winner = current_player
        print(f'Победил {winner}')

    is_draw = check_draw(gameboard)

    if is_draw:
        print('Ничья')

    return MoveResult(is_endgame=is_endgame, is_draw=is_draw)
 

def move_position(current_player: str) -> tuple[int, int]:
    position = make_bot_move() if current_player == CPU_NAME else make_players_move(current_player)
    return position


def get_current_player(player_name):
    player_plays_first = randint(0, 1)
    
    if player_plays_first:
        current_player = player_name
    else:
        current_player = CPU_NAME
    return current_player
