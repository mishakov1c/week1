from board import print_board
from checkings import check_draw, check_endgame
from config import COLUMNS, ROWS, EMPTY_BLOCK, O_MARK, X_MARK
from random import randint


class MoveResult():
    def __init__(self, endgame, is_draw):
        self.endgame = endgame
        self.is_draw = is_draw


def bot_move():
    position = f'{randint(0, COLUMNS - 1)}{randint(0, ROWS - 1)}'
    print(f'cpu делает ход {position}')
    return position


def players_move(player):
    move = input(f'{player}, сделайте ход.\n')
    while move_is_not_correct(move):
        move = input(f'{player}, сделайте корректный ход (2 цифры).\n')    

    return move


def move_is_not_correct(move):
    return ((len(move) != 2) or (not move.isnumeric())
        or (int(move[0]) > (ROWS - 1) or int(move[1]) > (COLUMNS - 1)))


def make_move(gameboard, queue, player, endgame, is_draw):
    for k, v in queue.items():
        position = move_position(player, v)
        
        while gameboard[position] != EMPTY_BLOCK:
            print(f'Клетка {position} занята, выберите другую.')
            position = move_position(player, v)
        
        gameboard[position] = k
        
        print_board(gameboard)
            
        endgame = check_endgame(gameboard)

        if endgame:
            winner = queue[k]
            print(f'Победил {winner}')
            break

        is_draw = check_draw(gameboard)

        if is_draw:
            print('Ничья')
            break

    return MoveResult(endgame=endgame, is_draw=is_draw)
 

def move_position(player, v):
    return players_move(v) if v == player else bot_move()


def queue_of_players(player_name, cpu_name):
    player_plays_first = randint(0, 1)
    
    if player_plays_first:
        queue = {X_MARK: player_name, O_MARK: cpu_name}
    else:
        queue = {X_MARK: cpu_name, O_MARK: player_name}

    print(f'Первым ходит {queue[X_MARK]}.')
    return queue
