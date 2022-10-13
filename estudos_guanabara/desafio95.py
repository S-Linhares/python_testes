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

    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())
print(60*'=')

for pos, valor in enumerate(jogadores):
    print(f'{pos:<3}', end='')

    for k, v in valor.items():
        print(f'{str(v):<15}', end='')

    print('\n', end='')
#print(f'O nome do jogador é: {jogador["nome"]}')
#print(f'Os gols, respectivamente, em cada partida foram: {jogador["gols"]}')
#print(f'O total de gols deste jogador foi: {jogador["total"]}')
#print(60*'=')
#print(f'O jogador {jogador["nome"]} jogou um total de {cont} partidas.')
#for i in range(0, cont):
#    print(f'\t=> Na partida {i+1}, fez {jogador["gols"][i]} gols')
#print(f'Foi um total de {jogador["total"]} gols.')
