'''
O exercicio deve contar o numero de digitos que um numero tem
'''


def number_length(a: int) -> int:
    a = str(a)
    return len(a)


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

# These "asserts" are used for self-checking and not for an auto-testing
print(number_length(10) == 2)
print(number_length(0) == 1)
print(number_length(4) == 1)
print(number_length(44) == 2)
print("Coding complete? Click 'Check' to earn cool rewards!")
