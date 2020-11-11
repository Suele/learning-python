"""
-Em python listas são os arrays em outras linguagens como em java.
-Em python as listas não possuem valor fixo e podem possuir qualquer tipo de dados, por exemplo posso ter uma lista com strings e ints juntos.
-As listas em python são representadas por [].

>>>>> METODOS DE LISTAS

***Para adicionar elementos no final da lista => append
-Com o append é possivel adicionar um elemento de cada vez ou uma lista de elementos => append(['Bernardo', 'Bento'])

***Para adicionar elementos interaveis utiliza-se o => extend(['Mario', 'Pedro']) ou extend('Jesus')
-Strings são interaveis ex: >>>>> ['Maria', 'Pedro', 'Joao', 'Suelen', 'Jose', ['Bernardo', 'Bento'], 'Mario', 'Pedro', 'J', 'e', 's', 'u', 's']
OBS: extend(12) => vai dar erro o certo seria extend([12, 14, 22])

***insert => Para inserir elementos em uma determinada posição.
OBS: Lembrando que o insert não exclue o elemento que está na posição, e sim o desloca para a proxima posição.
EX: listaNomes.insert(0, 'Luis')

***Para juntar listas => lista = lista1 + lista2

***Pop => remove o ultimo elemento da lista se não for passado um parametro e retorna o elemento removido ou
          se for passado um indice como parametro ele será removido e retornado.
          EX: lista.pop() ou lista.pop(2)



>>>>> METODOS que podemos utilizar em LISTAS   
      
*** Split => Transforma uma variavel do tipo string em uma lista.
    OBS: Os espaços em branco da string serão substituidos por virgulas.
    EX: descricaoDeUmCurso = 'Programação python essencial.'
        descricaoDeUmCurso = descricaoDeUmCurso.split()
        print('>>>> Descrição do curso com split: ', descricaoDeUmCurso)

*** Join => Para transformar uma lista para uma string.
    OBS: O join retorna uma nova string.
    EX: lista1 = ['Ṕrogramação', 'em', 'python', 'é', 'essencial']
        descricao = ' '.join(lista1)
        print('>>>>> Lista transformada para string', descricao)

"""

#listaNomes = ['Maria', 'Pedro', 'Joao']
#print('>>>>', listaNomes)
# listaNomes.append('Suelen')
# listaNomes.append('Jose')
# print('>>>>', listaNomes)

# # adiciona uma lista dentro de outra lista
# listaNomes.append(['Bernardo', 'Bento'])
# print('>>>>', listaNomes)

# listaNomes.extend(['Mario', 'Pedro'])
# print('>>>>>', listaNomes)
# listaNomes.extend('Jesus')
# print('>>>>>', listaNomes)

# listaNomes.insert(0, 'Luis')
# print(listaNomes)


# vai dar error TypeError: 'int' object is not iterable
# print(listaNomes.extend(12))

# print(listaNomes.pop())
# print(listaNomes)
# print(listaNomes.pop(2))
# print(listaNomes)

print()

descricaoDeUmCurso = 'Programação python essencial.'
print('>>>> Descrição do Curso: ', descricaoDeUmCurso)
print('Qual da variavel descricaoDeUmCurso: ', type(descricaoDeUmCurso))

print()

# O metodo split transforma a variavel descricaoDeUmCurso que era uma string
# em uma lista.
descricaoDeUmCurso = descricaoDeUmCurso.split()
print('>>>> Descrição do curso com split: ', descricaoDeUmCurso)
print('Qual o tipo da variavel descricaoDeUmCurso: ', type(descricaoDeUmCurso))

print()

# Transformar uma lista em uma string
lista1 = ['Ṕrogramação', 'em', 'python', 'é', 'essencial']
print('>>>> Lista1', lista1)
print('O tipo da lista1: ', type(lista1))

print()

# O metodo join transforma uma lista em uma string
# neste caso separando as palavras por espaços em branco
descricao = ' '.join(lista1)
print('>>>>> lista tranformada em string: ', descricao)
print('O tipo da variavel descricao: ', type(descricao))

print()
