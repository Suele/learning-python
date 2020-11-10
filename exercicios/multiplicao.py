"""
Você recebe um integer positivo. Sua função deve calcular o produto dos digitos excluindo qualquer Zeros.
Por exemplo: O numero dado é 123405. O resultado será 1*2*3*4*5=120 (Não esquece de excluir os Zeros).
"""


def checkio(number: int) -> int:
    produtoDaMultiplicacao = 1

    number = str(number)
    for t in number:
        if t != '0':
            t = int(t)
            produtoDaMultiplicacao *= t
    return produtoDaMultiplicacao


print(checkio(123405))
