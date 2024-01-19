import string


def encode_text(text: str, shift: int) -> str:
    encoded_text = ''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += string.ascii_letters
    alphabet += string.digits
    alphabet += string.punctuation
    alphabet += ' '
    alphabet = alphabet.replace("'", "")
    print(alphabet)
    
    for char in text:
        index = alphabet.find(char)
        if index == -1:  # когдаа элемент не найден в алфививте
            print('ошибка', char)
            return ''
        new_index = (index + shift) % len(alphabet)
        encoded_text += alphabet[new_index]

    return encoded_text
        

print(encode_text('Вася, привте 1000', 1))
