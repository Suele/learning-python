'''
Verifique se uma determinada string tem todos os símbolos em maiúsculas. 
Se a string estiver vazia ou não tiver nenhuma letra, 
a função deve retornar True.

Entrada: uma string.

Saída: um booleano.
'''


def remove_space(text):
    text_space = []
    for item in text:
        if item != ' ':
            text_space.append(item)
    return text_space


def is_all_upper(text: str) -> bool:
    contador = 0

    if text == '' or text.isnumeric():
        return True
    else:
        text = remove_space(text)
        for item in text:
            if item.isupper():
                contador = contador + 1
        if contador == text.__len__():
            return True
        else:
            return False


if __name__ == '__main__':
    # print("Example:")
    #print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert is_all_upper('ALL UPPER') == True
    #assert is_all_upper('all lower') == False
    #assert is_all_upper('mixed UPPER and lower') == False
    #assert is_all_upper('') == True
    #assert is_all_upper('Hi') == False
    assert is_all_upper('123') == True
    #print("Coding complete? Click 'Check' to earn cool rewards!")
