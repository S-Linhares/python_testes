jogador = {'nome': '', 'gols': [], 'total': 0, 'partidas': 0}
gols = list()
jogadores = list()

while True:
    jogador['nome'] = str(input('Informe o nome do jogador: '))
    jogador['partidas'] = int(input(f'Informe quantas partidas {jogador["nome"]} jogou: '))

    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos Gols ele fez na partida {i+1}: ')))
        jogador['total'] += gols[i]

    jogador['gols'] = gols[:]
    jogadores.append(jogador.copy())
    gols.clear()
    jogador['total'] = 0

    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())
print(60*'=')

print(f'{str("cod"):<4}', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
for pos, valor in enumerate(jogadores):
    print(f'{pos:<4}', end='')

    for v in valor.values():
        print(f'{str(v):<15}', end='')

    print('\n', end='')
print(60*'-')

while True:
    opcao = int(input('Mostrar dado de que jogador[999 para sair]? '))

    if opcao == 999:
        print('Saindo do programa...')
        break
    while (opcao != 999) and (opcao >= len(jogadores)):
        print('Opção inserida inválida. Tente novamente.')
        opcao = int(input('Mostrar dado de que jogador[999 para sair]? '))

    print(f'Dados do jogador {jogadores[opcao]["nome"]}:')
    for i in range(0, jogadores[opcao]['partidas']):
        print(f'No jogo {i+1} fez {jogadores[opcao]["gols"][i]} gols.')
    print(60*'-')
