from board import board, print_board
from constants import CPU_NAME
from enums import TicTacToeSymbol
from move import get_first_move_player, make_move
from player import Player


def play_game() -> None:
    print('Добро пожаловать в игру "Крестики-нолики"!')

    player_name = input('Игрок, введите имя\n')

    human_player = Player(name=player_name)
    cpu_player = Player(name=CPU_NAME)

    current_player = get_first_move_player(human_player, cpu_player)
    current_mark = TicTacToeSymbol.CROSS

    print(f'Первым ходит {current_player.name}.')

    gameboard = board()
    print_board(gameboard)

    is_endgame = False
    is_draw = False

    while not is_endgame and not is_draw:
        move_result = make_move(gameboard, current_player, current_mark, is_endgame, is_draw)
        is_endgame = move_result.is_endgame
        is_draw = move_result.is_draw
        current_player = human_player if current_player == cpu_player else cpu_player
        current_mark = (
            TicTacToeSymbol.NOUGHT if current_mark == TicTacToeSymbol.CROSS
            else TicTacToeSymbol.CROSS
        )


if __name__ == '__main__':
    play_game()
