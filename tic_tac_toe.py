from random import randint
from itertools import cycle


def bot_move():
    h_int = randint(1,3)
    h_string = "a" if h_int == 1 else "b" if h_int == 2 else "c"
    v_string = str(randint(1,3))
    coords = h_string + v_string 
    
    return coords


def my_board(board = None, field = None, value = ""):
    if board is None:
        board = {'a1':' ', 'b1':' ', 'c1':' ',
                'a2':' ', 'b2':' ', 'c2':' ', 
                'a3':' ', 'b3':' ', 'c3':' '
                 }

    if value:
        board[field] = value

    return board


def draw_board(board = None):    
    delimeter = f'\n_   _   _\n       \n'
    
    if board is None:
        first_row = f'a1 | b1 | c1'
        second_row = f'a2 | b2 | c2'
        third_row = f'a3 | b3 | c3'
    else:
        first_row = f"{board['a1']} | {board['b1']} | {board['c1']}"
        second_row = f"{board['a2']} | {board['b2']} | {board['c2']}"
        third_row = f"{board['a3']} | {board['b3']} | {board['c3']}"
    
    print(first_row + delimeter + second_row + delimeter + third_row) 


def game_finished(board, value):
    return ((board['a1'] == board['a2'] == board['a3']) and board['a1'] == value
        or (board['b1'] == board['b2'] == board['b3']) and board['b1'] == value
        or (board['c1'] == board['c2'] == board['c3']) and board['c1'] == value
        or (board['a1'] == board['b1'] == board['c1']) and board['a1'] == value
        or (board['a2'] == board['b2'] == board['c2']) and board['a2'] == value
        or (board['a3'] == board['b3'] == board['c3']) and board['a3'] == value
        or (board['a1'] == board['b2'] == board['c3']) and board['a1'] == value
        or (board['a3'] == board['b2'] == board['c1']) and board['c1'] == value)
            

def move_result(bot_move, move_properties):
    player = move_properties[0]
    return (bot_move() if player == 'cpu'
            else input(f'{player}, сделайте ход. Формат "буквацифра", например "a1".'))


def game_preparations(my_board):
    print('Добро пожаловать в игру "Крестики-нолики"!')

    player_name = input('Игрок, введите имя\n')

    new_board = my_board()

    print('Подбросим монетку. Орел - первым ходит игрок, решка - первым играет компьютер.'
        + 'Тот, кто ходит первым, играет крестиками.')

    player_plays_first = randint(0, 1)

    if player_plays_first:
        print(f'Выпал орел. Первым ходит {player_name}.')
        players_symbols = {player_name: 'x', 'cpu': 'o'}
    else:
        print('Выпала решка. Первым ходит компьютер.')
        players_symbols = {'cpu': 'x', player_name: 'o'}

    my_cycle = cycle(players_symbols.items())
    
    return new_board, my_cycle


def play_tic_tac_toe():

    new_board, my_cycle = game_preparations(my_board)

    end_game = False
 
    board = {}
    moves = []

    while (not end_game and len(moves) != 9):
        move_properties = next(my_cycle)
        player, symbol = move_properties
       
        print("********")
       
        move = move_result(bot_move, move_properties)
        board = board if len(board) else new_board 
        while (move in moves) or move not in board:
            print('Сделайте корректный ход.')
            move = move_result(bot_move, move_properties)
        moves.append(move)
       
        print(f'Ход {player}: {move}')
        print() 
        board = my_board(board, move, symbol)
        draw_board(board)
        print()

        end_game = game_finished(board, symbol)
    else:
        print(f"Конец игры. Победил {player}" if end_game else "Ничья.")

if __name__ == "__main__":
    play_tic_tac_toe()