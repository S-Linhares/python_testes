tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print(35*'-')
print('\t\tLISTAGEM DE PREÇOS')
print(35*'-')
for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]}', end='')
        print((25 - len(tupla[i]))*'.', end='')
    else:
        print(f'R$ {tupla[i]:>6.2f}')
print(35*'-')
