numero = int(input('Informe o numero que deseja: '))
conversao = int(input('\nInforme para qual base deseja converter o numero:'
                      '\n1 - binario'
                      '\n2 - octal'
                      '\n3 - hexadecimal\n'))
if conversao == 1:
    numero = bin(numero)
    print(f'\nNúmero convertido para binario: {numero[2:]}')
elif conversao == 3:
    numero = hex(numero)
    print(f'\nNumero convertido para hexadecimal: {numero[2:]}')
elif conversao == 2:
    numero = oct(numero)
    print(f'\nNúmero convertido para octal: {numero[2:]}')
else:
    print('Opção inválida!!!!')
