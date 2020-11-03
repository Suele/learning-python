print('Digite um numero para tabuada.')
number = int(input())
print()

for mult in range(0, 11):
    print(f'{number} x {mult} = {number * mult}')
