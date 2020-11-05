# Crie um programa que organize e imprima a lista a seguir colocando todos os 'R' juntos, depois todos os 'B' e por ultimo os 'G'.
# Ele também deve imprimir a versão da lista organizada em forma de string separada por ' - '
# A lista letras = ['R', 'B', 'R', 'R','B','G','G','B','G','R', ] deve gerar os 2 outputs abaixo
# ['R', 'R', 'R', 'R','B','B','B','G','G','G', ] e
# 'R - R - R - R - B - B - B - G - G - G'


listaLetras = ['R', 'B', 'R', 'R', 'B', 'G', 'G', 'B', 'G', 'R', ]

listaR = []
listaB = []
listaG = []

for lista in listaLetras:
    if lista in 'R':
        listaR.append('R')
    if lista in 'B':
        listaB.append('B')
    if lista in 'G':
        listaG.append('G')


print('>>>> listaR', listaR)
print('>>>> listaB', listaB)
print('>>>> listaG', listaG)

listaRBG = listaR + listaB + listaG
listaRBG.split('-')
