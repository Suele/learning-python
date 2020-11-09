''' Crie um programa que pede para o usuário adivinhar o nomero que ele está pensando.
O usuário pode dar palpites até acertar mas o programa deve seguir as seguintes instruções:
- O número deve ser entre 1 e 80, inclusivos e sorteado aleatóriamente
- O usuário deve receber dicas de acordo com seu palpite:
    - Se o palpite for até +/- 10 diferente do número, o programa deve dizer que o numero é "só um pouquinho maior/menor"
    - Se o palpite do mais que +/- 10 diferente do número, o programa deve dizer que o número é "muito' maior/menor" que o palpite
    - O programa deve dizer em quantas tentativas o usuário acertou. Se for 5 ou menos dizer 'parabens', se for 6 ou mais dizer 'finalmente'
    - O programa deve perguntar se o usuário quer jogar de novo e enquanto ele disser que sim o jogo deve continuar.'''

import random

print('Vamos brincar de advinha, voce terá que advinhar o numero que estou pensando')
print('Vou pensar em um numero de 1 a 25')
print()

contadorDeTentativas = 0

numeroQueEstouPensando = random.randint(1, 80)

voceQuerJogar = True

while voceQuerJogar == True:
    print('Qual é o seu palpite?')
    palpite = input()
    palpite = int(palpite)

    print('>>>> seu palpite foi : ', palpite)
    diferenca = (palpite - numeroQueEstouPensando)
    diferenca = diferenca.__abs__()
    print()
    if palpite == numeroQueEstouPensando:
        contadorDeTentativas += 1
        print(f'Parabens voce acertou na {contadorDeTentativas} tentativa')
        voceQuerJogar = False
    elif palpite > numeroQueEstouPensando:
        contadorDeTentativas += 1
        print(f'O seu palpite é maior do que o numero que estou pensando.')
        print(
            f'A diferença entre eles é {diferenca} numeros a menos no seu palpite')
        print()

    elif palpite < numeroQueEstouPensando:
        contadorDeTentativas += 1
        print(f'O seu palpite é menor do que o numero que estou pensando.')
        print(
            f'A diferença entre eles é {diferenca} numeros a mais no seu palpite')
        print()
