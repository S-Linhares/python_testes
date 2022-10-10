lista = []
for i in range(0, 5):
    num = int(input('Informe o número que deseja adicionar: '))
    if i == 0:
        lista.append(num)
        print('Número adicionado na posição ao final da lista.')
    else:
        for j in range(0, len(lista)):
            if lista[j] > num:
                lista.insert(j, num)
                print(f'Número adicionado na posição {j}')
                break
            elif j == (len(lista) - 1):
                lista.append(num)
                print('Número adicionado na posição ao final da lista.')
print(f'\nOs valores inseridos em ordem crescente: {lista}')
