lista = []
for i in range(0, 5):
    lista.append(input(f'Informe o valor que deseja adicionar a lista na posição {i}: '))
print(f'\nO maior valor da lista é: {max(lista)}. Ele está na posição: ', end='')
for pos, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{pos}... ', end='')
print(f'\nO menor valor da lista é: {min(lista)}. Ele está na posição: ', end='')
for pos, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{pos}... ', end='')
