import random
numero = random.randrange(0, 5)
user = int(input('Digite o numero que acha que foi pensado: '))
if user == numero:
    print('Você acertou!')
else:
    print(f'Você errou, perdeu! Pensei no número {numero}')
