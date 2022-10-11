matriz = [[], [], []]
soma_par = 0
soma_terceira = 0
maior_segunda = 0
for i in range(0, 9):
    if i < 3:
        matriz[0].append(int(input(f'Informe o número da linha 0/coluna {i}: ')))
        if (matriz[0][i] % 2) == 0:
            soma_par += matriz[0][i]
    if i >= 3 and i < 6:
        matriz[1].append(int(input(f'Informe o número da linha 1/coluna {i-3}: ')))
        if (matriz[1][i-3] % 2) == 0:
            soma_par += matriz[1][i-3]
    if i >=6 and i < 9:
        matriz[2].append(int(input(f'Informe o número da linha 2/coluna {i-6}: ')))
        if (matriz[2][i-6] % 2) == 0:
            soma_par += matriz[2][i-6]
for i in range(0, 3):
    soma_terceira += matriz[i][2]
print(60*'=')

print(f'| {matriz[0][0]:^5} | {matriz[0][1]:^5} | {matriz[0][2]:^5} |')
print(f'| {matriz[1][0]:^5} | {matriz[1][1]:^5} | {matriz[1][2]:^5} |')
print(f'| {matriz[2][0]:^5} | {matriz[2][1]:^5} | {matriz[2][2]:^5} |')

print(60*'=')
print(f'A soma de todos os valores pares: {soma_par}')
print(f'A soma dos valores da terceira coluna: {soma_terceira}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')