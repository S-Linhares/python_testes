import random
cont = 0
while True:
    cond = str(input('Escolha se deseja Par ou Ímapar [P/I]: ').upper())
    num = int(input('Escolha o número que quer jogar[0-5]: '))
    num_pc = random.randint(0, 5)
    print(f'\nPC joga: {num_pc}')
    if cond == 'P':
        if (num_pc + num) % 2 == 0:
            print('Rodada ganhada!')
            cont += 1
        else:
            print(f'Você perdeu! Com um total de {cont} vitorias consecutivas')
            break
    elif cond == 'I':
        if (num_pc + num) % 2 == 0:
            print(f'Você perdeu! Com um total de {cont} vitorias consecutivas')
            break
        else:
            print('Rodada ganhada!')
            cont += 1

