from board import print_board
from checkings import check_draw, check_endgame
from config import NUM_OF_CELLS
from constants import CPU_NAME
from enums import TicTacToeSymbol
from player import Player
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


def make_players_move(player: Player) -> tuple[int, int]:
    raw_move = input(f'{player.name}, сделайте ход.\n')

    while True:
        raw_move_is_numeric = raw_move.isnumeric()
        if not raw_move_is_numeric or len(raw_move) != 2:
            raw_move = input(
                f'{player.name}, сделайте корректный ход (2 цифры).\n')
        else:
            move = (int(raw_move[0]), int(raw_move[1]))
            if move_is_correct(move):
                break

    return move


def move_is_correct(move: tuple[int, int]) -> bool:
    return (
        int(move[0]) <= (NUM_OF_CELLS - 1)
        and int(move[1]) <= (NUM_OF_CELLS - 1)
    )


def make_move(
    gameboard: list[list[TicTacToeSymbol]],
    current_player: Player,
    current_mark: TicTacToeSymbol,
    is_endgame: bool,
    is_draw: bool
) -> MoveResult:

    row, column = get_move_position(current_player)

    while gameboard[row][column] != TicTacToeSymbol.EMPTY:
        print(
            f'Клетка {row}{column} занята, выберите другую.')
        row, column = get_move_position(current_player)

    gameboard[row][column] = current_mark

    print_board(gameboard)

    is_endgame = check_endgame(gameboard)

    if is_endgame:
        # winner = current_player
        print(f'Победил {current_player.name}')
    else:
        is_draw = check_draw(gameboard)
        if is_draw:
            print('Ничья')

    return MoveResult(is_endgame=is_endgame, is_draw=is_draw)


def get_move_position(current_player: Player) -> tuple[int, int]:
    position = (
        make_bot_move() if current_player.name == CPU_NAME else make_players_move(current_player)
    )
    return position


def get_first_move_player(human_player: Player, cpu_player: Player) -> Player:
    human_player_plays_first = randint(0, 1)

    if human_player_plays_first:
        current_player = human_player
    else:
        current_player = cpu_player
    return current_player
