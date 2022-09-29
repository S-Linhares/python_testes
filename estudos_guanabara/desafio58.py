import random
numero = random.randrange(0, 10)
user = -1
tentativas = 0
while user != numero:
    tentativas += 1
    user = int(input('Digite o numero que acha que foi pensado: '))
    if user == numero:
        print(f'Você acertou em {tentativas} tentativas! Pensei no número {numero}')
    else:
        print(f'Você errou, perdeu! Tente novamente.')
