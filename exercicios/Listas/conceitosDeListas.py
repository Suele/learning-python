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

"""

listaNomes = ['Maria', 'Pedro', 'Joao']
print('>>>>', listaNomes)
listaNomes.append('Suelen')
listaNomes.append('Jose')
print('>>>>', listaNomes)

# adiciona uma lista dentro de outra lista
listaNomes.append(['Bernardo', 'Bento'])
print('>>>>', listaNomes)

listaNomes.extend(['Mario', 'Pedro'])
print('>>>>>', listaNomes)
listaNomes.extend('Jesus')
print('>>>>>', listaNomes)

# vai dar error TypeError: 'int' object is not iterable
print(listaNomes.extend(12))
