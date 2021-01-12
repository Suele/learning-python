"""
-Em python os dados vindo do input são strings sendo assim necessario
 converter os valores para int ou float.

-Em python o tamanho dos números são do tamanho da menoria disponivel 
no computador.Não ocorrendo estouro de menoria como em java.
"""

a = int(input('Entre com o primeiro número: '))
b = int(input('Entre com o segundo número.'))


print(a, type(a))
print(b, type(b))

soma = a + b

print(soma, type(soma))

c = float(input('Digite o primeiro número: '))
d = float(input('Digite o seu segundo número: '))

print(c, type(c))
print(d, type(d))
