'''
Tipo Booleano
É True ou False, com a primeira letra em maiuscula.


Retornam valores booleanos:  
- Condicionais(if, else, elif)
- Operadores Logicos(and(E), or(OU), not(negação))
- Operadores de comparação(==, !=, >, < >=, <=)
- Operadores Identidade(is, is not)

'''
print()
# uso com condicionais
usuarioAtivo = True

if usuarioAtivo:
    print('O usuario está ativo')
else:
    print('O usuario não está ativo')

print()

# uso com not(negação)
usuarioMaiorIdade = True
print('usuário é maior de idade: ', not usuarioMaiorIdade)
print()

# Operador or(ou)
print('---> True or True é: ', True or True)
print('---> True or False é: ', True or False)
print('---> False or True é: ', False or True)
print('---> False or False é: ', False or False)

print()
# Operador and(E)
print('---> True and True é: ', True and True)
print('---> True and False é: ', True and False)
print('---> False and True é: ', False and True)
print('---> False and False é: ', False and False)

print()

# Operador identidade(is ou is not)
# compara os enderecos de memoria dos objetos
# se forem o mesmos endereço de memoria então é o mesmo objeto e
# retorna true.
# Não pode ser substituido pelo ==
nomes = ['Maria', 'Pedro', 'Jose']

nome1 = 'Maria'

print('nome1 is nomes: ', nome1 is nomes)
print('Maria is nomes: ', 'Maria' is nomes)
print('nomes[1] in nomes: ', nomes[1] in nomes)

print()

# Operador de associação
# Verifica se os elemntos têm os valores iguais
# Pode ser substituido pelo ==
frutas = ['maçã', 'banana', 'pera', 'melancia']
fruta1 = 'maçã'
fruta2 = 'acerola'

print('fruta1 in frutas: ', fruta1 in frutas)
print('fruta1 in frutas: ', fruta1 == frutas[0])
print('fruta2 in frutas: ', fruta2 in frutas)
