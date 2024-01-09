name = 'Илья Муромец'

way1 = False
way2 = False
way3 = False

while way1 == False or way2 == False or way3 == False:
    print(name, 'приехал к камню. На нем надпись:')
    if way1 == False:
        print('Налево пойдешь - убит будешь,')
    if way2 == False:
        print('Прямо пойдешь - женат будешь,')
    if way3 == False:
        print('Направо пойдешь - богатым будешь!')

    way = input('В какую сторону ехать?')

    if way == 'налево':
        if way1 == False:
            print(name, 'встретил разбойников.')
            action1 = input('Что делать?')
            if action1 == 'играть в карты':
                print(name, 'победил их. Он свободен!')
                way1 = True
            elif action1 == 'присоеденится к ним':
                print(name, 'теперь тоже разбойник!')
                break
            elif action1 == 'побить их':
                print(name, 'избил их. Они сбежали.')
                way1 = True
            elif action1 == 'бежать':
                print(name, 'не достаточно быстр!')
                break
            elif action1 == 'договорится':
                print(name, 'не смог договорится!')
                break
            else:
                print(name, 'не может это сделать.')
                break
        else:
            print(name, 'тут был!')
            
    elif way == 'прямо':
        if way2 == False:
            print(name, 'окружон девушками!')
            action2 = input('Что делать?')
            if action2 == 'отдаться им':
                print(name, 'согрeшил!')
                break
            elif action2 == 'бежать':
                print(name, 'не достаточно быстр!')
                break
            elif action2 == 'побить их':
                print(name, 'не бьет женщин!')
            elif action2 == 'соврать им':
                print(name, 'сделал вид, что отдался им.')
                print('Когда ложился на кровать сначала бросил туда девушку')
                print('Она проволилась в погриб, где уже сидели некоторые богатыри')
                action22 = input('Что делать с богатырями?')
                if action22 == 'освободить':
                    print(name, 'освободил всех богатырей!')
                elif action22 == 'убить':
                    print(name, 'убил всех богатырей!')
                elif action22 == 'ничего':
                    print(name, 'оставил богатырей!')
                else:
                    print(name, 'не может это сделать.')
                action23 = input('Что делать с девушкой?')
                if action23 == 'отпустить':
                    print(name, 'отпустил её. Она зашла ему за спину и перерезала горло!')
                    break      
                elif action23 == 'убить':
                    print(name, 'убил её!')
                    way2 = True
                elif action23 == 'оставить':
                    print(name, 'оставил её гнить в погребе')
                    way2 = True
                else:
                    print(name, 'не может это сделать.')
                    break
            else:
                print(name, 'не может это сделать.')
                break
        else:
            print(name, 'тут был!')
            
    elif way == 'направо':
        if way3 == False:
            print(name, 'нашол мешок золота')
            action3 = input('Что делать?')
            if action3 == 'пожертвовать':
                print(name, 'пожертвовал все на храмы.')
                way3 = True
            elif action2 == 'ничего':
                print(name, 'умер в нищите!')
            elif action2 == 'оставить себе':
                print(name, 'оставил деньгисебе и спился!')
                break
            else:
                print(name, 'не может это сделать.')
                break         
        else:
            print(name, 'тут был!')
            
    else:
        print('Нет такой дороги=(')

print('Сказке конец.')

#можно изменение имени добавить.
#и не просто 'сказке конец', а разнаобразия  
