'''
+ поле из 9 клеток
+ игрок_1 - X
+ игрок_2 - 0
игроки ходят по очереди
начинает X
победа:
    3 одинаковых по горизонтали, вертикали или диагонали
ничья - нет свободны клеток и нет победителя
'''
#диагонали немного не работют
#где используют тот def на котором остановились

import os
from random


def draw_filed(field: list) -> None:
    ''' Выводит на экран три ряда игрового поля '''
    os.system('cls')
    for i in range(0, 7, 3):
        print(field[i], field[i + 1], field[i + 2])


def make_move(field: list, player: str):
    '''
    Спрашивает номер клетки поля: 1-9 вкл
    Проверяет, есть ли на поле клетка с таким номером
    Проверяет, что клетка с этим номером свободна
    Если пройдет все проерки, ставит игрока в эту клетку
    '''
    while True:
        cell_num = int(input('Введите номер клетки (1-9): '))
        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер должен быть от 1 до 9 вкл.')
            continue
        if field[cell_num - 1] in players:
            print('Ошибка! Эта клетка занята.')
            continue
        field[cell_num - 1] = player
        break

    def make_move_computer(field: list, player: str) -> None:
        '''
        Собрать клетки, куда можно ходить:
            на поле
            пустые
        Выбрать случайную из них
        Сделвть туда ход
        '''
        emply_cells_indexes = []
        for i in range(9):
            if not field[i] if players:
                emply_cells_indexes.append(i)
            # TODO: с помощью чёйса выбрать случайную клетку из свободных



def get_winner(fied: list, player: str) -> str:
    #горизонтали
    for i in range(0, 7, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            return player

    #вертикали
    for i in range(0, 3, 1):
        if field[i] == field[i + 3] == field[i + 6] == player:
            return player

    #диагонали
    for i in range(0,):
        if field[i] == field[i + 4] == field[i + 8] == player:
            return player


    for i in range(2):
        if field[i + 2] == field[i + 4] == field[i + 5] == player:
            return player


    return ''


player_1 = 'X'
player_2 = '0'
players = (player_1, player_2)
field = list(range(1, 10, 1))
moves = 1

while True:
    if moves > 9:
        print('Ничья')
        break
    draw_filed(field)
    if moves % 2:
        player = player_1
    else:
        player = player_2
    make_move(field, player)
    moves += 1
    winner = get_winner(field, player)
    if winner:
        draw_filed(field)
        print('Победил', winner)
        break



print('Игра окончена.')
