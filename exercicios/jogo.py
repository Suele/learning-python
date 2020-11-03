"""
Homework Aula 1 - Um jogo

- Criar um programa que pegue nome do usuário e explique as regras do jogo para o usuário.
- Pense em um numero de 1 a 20
- Sortear um numero aleatório
- Usuário tente adivinha numero sorteado
- Usuário só pode ter 6 chances
- Pegar cada palpite e verificar se é: maior, igual ou menor que o número sorteado
- Falar mensagem que o número que o usuário deu palpite é maior, igual ou menor que o número sorteado.
- Colocar condição de parada "break" nas condições de verificação 
"""
import random


print('Qual seu nome?')
use_name = input()
print()
print(f'Estou pensando em um numero de 1 a 20, e voce tem 6 tentativas.')
print()
numero = random.randint(1, 20)
for tentativa in range(1, 7):
    print('qual numero estou pensando? ')
    palpite = int(input())
    if palpite == numero:
        print('Voce acertou')
        break
    elif palpite < numero:
        print('O numero é maior')
    elif palpite > numero:
        print('Tenta um numero menor')
if palpite != numero:
    print(f'Voce não acertou o numero escolhido era:', {numero})
