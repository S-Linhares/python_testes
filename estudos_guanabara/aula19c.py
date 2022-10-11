estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil: #for para a lista
    for k, v in e.items(): #for para dicionario
        print(f'O campo {k} tem valor {v}')
print('\n')
for e in brasil: #for para a lista
    for v in e.values(): #for para dicionario
        print(v, end='')
    print('\n', end='')
print('\n')
