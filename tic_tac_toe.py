from random import randint

print('Добро пожаловать в игру "Крестики-нолики"')

# play = input('Хотите сыграть? Y, n\n')

# if play != 'Y':
#     print('Приходите еще!')
# else:
#     print('Играем!')

def bot_move():

    h_int = randint(1,3)
    h_string = "a" if 1 else "b" if 2 else "c"

    v_string = str(randint(1,3))

    coords = h_string + v_string 

    return coords

def board(field = None, value = ""):
    
    first_row = f'a1 | a2 | a3'
    delimeter = f'\n_   _   _\n       \n'
    second_row = f'b1 | b2 | b3'
    third_row = f'c1 | c2 | c3'
    
    board = first_row + delimeter + second_row + delimeter + third_row

    if value:
        board = board.replace(field, value)

    return board

print(board())

print('Подбросим монетку. Орел - первым ходит игрок, решка - первым играет компьютер. Тот, кто ходит первым, играет крестиками.')

player_plays_first = randint(0, 1)
    
print('Выпао орел. Первым ходит игрок.' if player_plays_first else 'Выпала решка. Первым ходит компьютер.')

end_game = False

count = 0 

while count != 10:
    print(board(bot_move(), 'x'))
    count += 1


