import random
import time
jogadores = {'jogador 1': random.randint(1, 6),
             'jogador 2': random.randint(1, 6),
             'jogador 3': random.randint(1, 6),
             'jogador 4': random.randint(1, 6)}

for id, valor in jogadores.items():
    print(f'{id} jogou o dado e tirou: {valor}')
print('\nMontando o ranking dos jogadores', end='')
time.sleep(0.33)
print('.', end='')
time.sleep(0.33)
print('.', end='')
time.sleep(0.33)
print('.', end='')
time.sleep(0.33)
print('\n', end='')
print(30*'=')
print(10*' ', 'RANKING')
print(30*'=')
p = 1
for i in sorted(jogadores, key = jogadores.get, reverse = True):
    print(f'{p}º lugar: {i}, com um {jogadores[i]}')
    p += 1
