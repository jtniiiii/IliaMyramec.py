import os  # для очистки экрана
from random import randint

# def = функция
'''
Не работает
 скорей всего дело в листах
Сделать pause
'''

def start_game():
    ''' Создает игрока и отправляет его к кмню '''
    player_name  = input('Ведите имя игрока: ')
    max_hp = 100
    player_hp = 100
    player_maney = 50
    player_xp = 0 
    player_level = 1
    potion = 0
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    visit_rock(list)

def show_hero(max_hp, name, hp, money, xp, level, potion):
    '''Выводит на экран информацию о персонаже'''
    print('-' * 20)
    print('имя:', name)
    print('здоровье:', hp)
    print('деньги:', money)
    print('зелья:', potion)
    print('опыт:', xp)
    print('уровень:', level)
    print('-' * 20)




def visit_rock(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Камень '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    print(player_name, 'приехал к камню')
    print('1 - Поехать на арену')
    print('2 - Отправится в таверну')
    print('3 - Заглянуть в лавку')
    if potion > 0:
        print('9 - Выпить зелье')
    print('0 - Выйти из игры')
    option = input('Ведите номер варианта: ')
    if option == '1':
        visit_aren(list)
        visit_rock(list)
        return list
    elif option == '2':
        visit_tavern(list)
        visit_rock(list)
        return list
    elif option == '3':
        visit_lavka(list)
        visit_rock(list)
        return list
    elif potion > 0:
        if option == '9':
            location = 0
            drink_potion(list, location)
            visit_rock(list)
            return list
    elif option == '0':
        pass
    else:
        visit_rock(list)
        return list



def visit_aren(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Арена '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    print(player_name, 'приехал на арену')
    print('1 - Сражатся')
    print('2 - Вернутся к камню')
    if potion > 0:
        print('9 - Выпить зелье')
    print('0 - Выйти из игры')
    option = input('Ведите номер варианта: ')
    if option == '1':
        battle(list)
        visit_aren(list)
        return list
    elif option == '2':
        return list
    elif potion > 0:
        if option == '9':
            location = 1
            drink_potion(list, location)
            visit_aren(list)
            return list
    elif option == '0':
        pass
    else:
        visit_aren(list)
        return list

def battle(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Бой '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    enemay_hp = player_hp - 50
    while enemay_hp >= 0 or player_hp >= 0:
        player_damag = randint(0, 10)
        enemay_hp -= player_damag
        print(player_name, 'наносит', player_damag, 'урона врагу')
        if enemay_hp <= 0:
            break
        else:
            print('У врага ещё', enemay_hp, 'здаровья')
            enemay_damag = randint(0, 10)
            player_hp -= enemay_damag
            print('Враг наносит', enemay_damag, 'урона', player_name)
            if player_hp <= 0:
                break
            else:
                print('У', player_name, 'осталось', player_hp, 'здаровья')
                continue
    if enemay_hp <= 0:
        player_xp += 100
        new_level = player_level * 100   # то сколько нужно xp для повышения level
        if player_xp >= new_level:
            player_level += 1
            player_xp -= new_level
            max_hp += 50
            player_hp = max_hp
        player_maney += 30
        show_hero(list)
        while option == 1 or option == 2:
            print('Вы выграли!')
            print('1 - Вернутся')
            print('0 - Выйти из игры')
            option = input('Ведите номер варианта: ')
            if option == 1:
                return list
            elif option == '0':
                pass
            else:
                os.system('cls')  # очищает экран
                continue
    elif player_hp <= 0:
        while option == 1 or option == 2:
            print('Вы умерли')
            print('1 - Начать с начала')
            print('0 - Выйти из игры')
            option = input('Ведите номер варианта: ')
            if option == '1':
                start_game()
            elif option == '0':
                pass
            else:
                os.system('cls')  # очищает экран
                continue
    



def visit_tavern(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Таверна '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    print(player_name, 'пришол в таверну')
    print('1 - Играть в кости')
    print('2 - Вернутся к камню')
    if potion > 0:
        print('9 - Выпить зелье')
    print('0 - Выйти из игры')
    option = input('Ведите номер варианта: ')
    if option == '1':
        plase_bid(list)
        visit_tavern(list)
        return list
    elif option == '2':
        return list
    elif potion > 0:
        if option == '9':
            location = 2
            drink_potion(list, location)
            visit_tavern(list)
            return list
    elif option == '0':
        pass
    else:
        visit_tavern(list)
        return list

def plase_bid(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Ставка '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    bid = int(input('Ваша ставка: '))
    if bid > 0 and bid <= player_maney:
        play_dicel(list)
    elif bid <= 0:
        while option == 1 or option == 2 or option == 0:
            print('Ставка должна быть больше 0')
            print('1 - Поставить')
            print('2 - Вернутся')
            print('0 - Выйти из игры')
            option = input('Ведите номер варианта: ')
            if option == '1':
                plase_bid(list)
                return list
            elif option =='2':
                return list
            elif option == '0':
                pass
            else:
                os.system('cls')  # очищает экран
                continue
    elif bid > player_maney:
        while option == 1 or option == 2 or option == 0:
            print('У', player_name, 'столько нет')
            print('1 - Поставить')
            print('2 - Вернутся')
            print('0 - Выйти из игры')
            option = input('Ведите номер варианта: ')
            if option == '1':
                plase_bid(list)
                return list
            elif option =='2':
                return list
            elif option == '0':
                pass
            else:
                os.system('cls')  # очищает экран
                continue

def play_dicel(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion, bid):
        ''' Игра в кости '''
        player_score = randint(1, 12)
        enemy_score = randint(1, 12)
        if player_score > enemy_score:
            player_maney += bid
            os.system('cls')  # очищает экран
            list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
            show_hero(list)
            print(player_name, 'выбросил', player_score)
            print('Тактирщик выбросил', enemy_score)
            print(player_name, 'победил')
        elif enemy_score > player_score:
            player_maney -= bid
            os.system('cls')  # очищает экран
            show_hero(list)
            print(player_name, 'выбросил', player_score)
            print('Тактирщик выбросил', enemy_score)
            print(player_name, 'проиграл')
        else:
            os.system('cls')  # очищает экран
            show_hero(list)
            print(player_name, 'выбросил', player_score)
            print('Тактирщик выбросил', enemy_score)
            print('Ничья')
        print('1 - Сыграть ещё')
        print('2 - Вернутся')
        print('0 - Выйти из игры')
        option = input('Ведите номер варианта: ')
        if option == '1':
            plase_bid(list)
            return list
        elif option == '2':
            return list
        if option == '0':
            pass
        else:
            return list


def visit_lavka(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Лавка '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    print(player_name, 'заглянул в лавку')
    print('1 - Купить зелье')
    print('2 - Вернутся к камню')
    if potion > 0:
        print('9 - Выпить зелье')
    print('0 - Выйти из игры')
    option = input('Ведите номер варианта: ')
    if option == '1':
        buy_potion(list)
        visit_lavka(list)
        return list
    elif option == '2':
        return list
    elif potion > 0:
        if option == '9':
            drink_potion(list)
            visit_lavka(list)
            return list
    elif option == '0':
        pass
    else:
        visit_lavka(list)
        return list

def buy_potion(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Зелья '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    if player_maney >= 25:
        player_maney -= 25
        potion += 1
        return list
    elif player_maney < 25:
        print('Не хватает денег')
        print('1 - Вернутся')
        print('0 - Выйти из игры')
        option = input('Ведите номер варианта: ')
        if option == '1':
            return list
        elif option == '0':
            pass
        else:
            return list




def drink_potion(max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion):
    ''' Питье зелья '''
    os.system('cls')  # очищает экран
    list[max_hp, player_name, player_hp, player_maney, player_xp, player_level, potion]
    show_hero(list)
    player_hp += 30
    potion -= 1
    if player_hp > max_hp:
        player_hp = max_hp
    return list


start_game()
