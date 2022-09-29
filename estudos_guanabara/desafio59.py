n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('\nMENU:')
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos números')
    print('5 - Finalizar programa')
    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma é {soma}')
    elif opcao == 2:
        multi = n1 * n2
        print(f'A multiplicação é {multi}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número é {maior}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Saindo do programa...')
