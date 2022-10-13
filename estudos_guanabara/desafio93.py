jogador = dict()
jogador['nome'] = str(input('Informe o nome do jogador: '))
cont = int(input(f'Informe quantas partidas {jogador["nome"]} jogou: '))
jogador['gols'] = list()
jogador['total'] = 0
for i in range(0, cont):
    jogador['gols'].append(int(input(f'Quantos Gols ele fez na partida {i+1}: ')))
    jogador['total'] += jogador['gols'][i]
print(60*'=')
print(f'O nome do jogador é: {jogador["nome"]}')
print(f'Os gols, respectivamente, em cada partida foram: {jogador["gols"]}')
print(f'O total de gols deste jogador foi: {jogador["total"]}')
print(60*'=')
print(f'O jogador {jogador["nome"]} jogou um total de {cont} partidas.')
for i in range(0, cont):
    print(f'\t=> Na partida {i+1}, fez {jogador["gols"][i]} gols')
print(f'Foi um total de {jogador["total"]} gols.')
