'''
Faça um programa que verifica se a senha fornecida é maior
que seis caracteres.
'''


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False


# These "asserts" are used for self-checking and not for an auto-testing
assert is_acceptable_password('short') == False
assert is_acceptable_password('muchlonger') == True
assert is_acceptable_password('ashort') == False
print("Coding complete? Click 'Check' to earn cool rewards!")
