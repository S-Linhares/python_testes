import random
lista = list()
jogo = list()
num = int(input('Quantos jogos deseja fazer: '))
for i in range(0, num):
    for i in range(0, 6):
        jogo.append(random.randint(0, 60))
    lista.append(jogo[:])
    jogo.clear()

for i in range(0, num):
    lista[i].sort()
    print(f'Jogo {i+1}: {lista[i]}')
