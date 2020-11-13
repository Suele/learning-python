''' 
Tuplas => Tuple

- As tuplas são representadas por ()
- As tuplas são imutaveis, ou seja não podemos altera-las.

OBS: Tuplas com apenas um elemento devem ser representadas   
  

'''

print()

tupla1 = (1, 2, 3, 4, 5)
print(type(tupla1))
print('>>>>> Tupla1:', tupla1)

print()

# Isso não é uma tupla apesar do elemento estar entre parentese
# O tipo retorna que o elemento é um inteiro.
tupla2 = (6)
print(type(tupla2))
print('>>>>>> Tupla2', tupla2)

print()

# Isso é uma tupla
# Quando tem apenas um elemento entre parenteses
# Deve-se colocar a virgula apos o elemento mesmo que não tenha.
tupla3 = (6,)
print(type(tupla3))
print('>>>>>> Tupla3', tupla3)

print()

# Uma tupla vazia é uma tupla.
tupla4 = ()
print(type(tupla4))
print('>>>>>> Tupla4: ', tupla4)

print()
