valores = []
qtd = 0
while True:
    valores.append(int(input('Informe o valor que deseja adicionar: ')))
    qtd += 1
    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())
valores.sort(reverse = True)
print(60*'=')
print(f'Os valores digitados em ordem descrescente foram: {valores}')
print(f'Foram digitados {qtd} elementos')
if 5 in valores:
    print('O valor 5 está incluson na lista')
else:
    print('O valor 5 não está incluso na lista')
