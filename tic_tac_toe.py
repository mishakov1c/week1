from board import board, print_board
from move import make_move, queue_of_players


def play_game():
    print('Добро пожаловать в игру "Крестики-нолики"!')

    player_name = input('Игрок, введите имя\n')
    cpu_name = 'cpu'

    queue = queue_of_players(player_name, cpu_name)

    gameboard = board()
    print_board(gameboard)
    
    is_endgame = False
    is_draw = False

    while not is_endgame and not is_draw:
        move_result = make_move(gameboard, queue, player_name, is_endgame, is_draw)
        is_endgame = move_result.endgame
        is_draw = move_result.is_draw

if __name__ == '__main__':
    play_game()
