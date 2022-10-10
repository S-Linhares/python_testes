pessoa = list()
pessoas = list()
maior = 0
menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if maior == menor == 0:
        maior = menor = pessoa[1]
    elif pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor:
        menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())
print(60*'=')

print(f'O maior peso foi de {maior}Kg. As pessoas com este peso são: ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]}... ', end='')
print('\n', end='')

print(f'O menor peso foi de {menor}Kg. As pessoas com este peso são: ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'{i[0]}... ', end='')
print('\n', end='')

print(f'Foram cadastradas {len(pessoas)} pessoas')
