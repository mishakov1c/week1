from board import board, print_board
from constants import CPU_NAME
from enums import TicTacToeSymbol
from move import get_current_player, make_move


def play_game() -> None:
    print('Добро пожаловать в игру "Крестики-нолики"!')

    player_name = input('Игрок, введите имя\n')

    current_player = get_current_player(player_name)
    current_mark = TicTacToeSymbol.X

    print(f'Первым ходит {current_player}.')

    gameboard = board()
    print_board(gameboard)
    
    is_endgame = False
    is_draw = False

    while not is_endgame and not is_draw:
        move_result = make_move(gameboard, current_player, current_mark, is_endgame, is_draw)
        is_endgame = move_result.is_endgame
        is_draw = move_result.is_draw
        current_player = player_name if current_player == CPU_NAME else CPU_NAME
        current_mark = TicTacToeSymbol.O if current_mark == TicTacToeSymbol.X else TicTacToeSymbol.X


if __name__ == '__main__':
    play_game()
