"""
Media das notas.
"""

print('Quantas notas voce quer digitar.')
notas = int(input())
print('')
somaDasNotas = 0

for item in range(0, notas):
    print(f'Digite a {item+1}ª nota ')
    nota = int(input())
    somaDasNotas += nota

mediaFinal = somaDasNotas / notas

print('')
if mediaFinal >= 70:
    print(
        f'Parabens voce foi aprovado sua media final foi: {mediaFinal}')
else:
    print(
        f'Vejo voce no proximo semestre sua media final foi: {mediaFinal}')
