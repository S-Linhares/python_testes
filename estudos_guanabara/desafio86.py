matriz = [[], [], []]
for i in range(0, 9):
    if i < 3:
        matriz[0].append(int(input(f'Informe o número da linha 0/coluna {i}: ')))
    if i >= 3 and i < 6:
        matriz[1].append(int(input(f'Informe o número da linha 1/coluna {i-3}: ')))
    if i >=6 and i < 9:
        matriz[2].append(int(input(f'Informe o número da linha 2/coluna {i-6}: ')))
print(60*'=')
print(f'| {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} |')
print(f'| {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} |')
print(f'| {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} |')