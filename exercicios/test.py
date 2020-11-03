print("Ola, qual seu nome?")
user_nome = input()
print(f"{user_nome}, em que ano voce nasceu?")
user_ano = input()
print(f'{user_nome}, vc ja fez aniversario esse ano? (Sim/Nao)')
user_aniv = input()
if user_aniv == 'Sim' or user_aniv == 'sim':
    user_idade = 2020 - int(user_ano)
    print(f"{user_nome}, voce ja fez aniversario, vc tem {user_idade} aninhos")
elif user_aniv == 'Nao' or user_aniv == 'nao':
    user_idade = 2020 - int(user_ano) - 1
    print(f"{user_nome}, se voce nao fez aniversario, vc tem {user_idade} aninhos")
