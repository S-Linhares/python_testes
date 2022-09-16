import random
numero = random.randrange(0, 5)
print(numero)
user = int(input('Digite o numero que acha que foi pensado: '))
if user == numero:
    print('Você acertou!')
else:
    print('Você errou, perdeu!')
