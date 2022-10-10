valores = []
while True:
    num = int(input('Informe o valor que deseja adicionar: '))
    if num in valores:
        print('Não será adicionado. Este número já está incluido!')
    else:
        valores.append(num)
        print('Número adicionado!')
    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())
valores.sort()
print(f'Os valores digitados foram: {valores}')
