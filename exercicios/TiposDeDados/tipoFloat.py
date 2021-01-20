"""
Tipo float - contem casas decimais

OBS: O separador das casas decimais é o ponto(.) não a virgula por ser 
o padrão americano. Se for utilizado virgula(,) o python entende ser 
uma tupla os elementos e não gera erro. 

conversão - float --> int fica apenas a parte inteira ou seja as casas 
decimais são perdidas.


"""
valor1 = 1, 44  # para o python é uma tupla
valor2 = 1.44  # para o python é um número do tipo float

print(type(valor1))
print(type(valor2))

print(int(valor2))  # só fica a parte inteira

print(valor2)
