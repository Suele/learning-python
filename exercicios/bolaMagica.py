import random

print('Seja bem vindo a bola magica')
print()

bolaMagica = ['sim',
              'provavelmente sim', 'não', 'sem duvida que sim', 'talvez', 'concentre-se e pergunte novamente', 'estou sentindo que sim', 'não crie espectativas']

continuaJogando = True

while continuaJogando == True:
    print('Digite sua pergunta para a bola magica')
    pergunta = input()
    respostaDaBolaMagica = random.choice(bolaMagica)
    print('>>>>>> resposta da bola magica: ', respostaDaBolaMagica)
    print()

    print('Voce deseja fazer outra pergunta para a bola magica?')
    print("Digite Sim ou Não")
    suaResposta = input()
    print()

    suaResposta = suaResposta.upper()

    if suaResposta == 'SIM' or suaResposta == 'S':
        continuaJogando = True
    else:
        print('Fim da consulta')
        continuaJogando = False
