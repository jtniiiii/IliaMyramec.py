import string

'''
Не пытайся понять.. тут даже я непонимаю
Эта программа кодирует текст, и возвращает его обратно
Ведии текст вконце и ниже его зашифрованую версию
+ смещение
'''


def encode_text(text: str, shift: int) -> str:
    ''' Если текст пустой '''
    if not text
        return text
    ''' Создание алфавита '''
    encoded_text = ''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += string.ascii_letters
    alphabet += string.digits
    alphabet += string.punctuation
    alphabet += ' '
    alphabet = alphabet.replace("'", "")
    
    for char in text:
        index = alphabet.find(char)
        if index == -1:  # когда элемент не найден в алфививте
            print('ошибка', char)
            return ''
        new_index = (index + shift) % len(alphabet)
        encoded_text += alphabet[new_index]

    return encoded_text
        

print(encode_text('Вася, привет 1000', 1))
print(encode_text('ГбтА-арсйгёуа2111', -1))