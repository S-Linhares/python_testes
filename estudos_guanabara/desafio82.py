valores = []
valores_par = []
valores_impar = []
while True:
    valores.append(int(input('Informe o valor que deseja adicionar: ')))
    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())

for i in range(0, len(valores)):
    if (valores[i] % 2) == 0:
        valores_par.append(valores[i])
    else:
        valores_impar.append(valores[i])
print(60*'=')
print(f'Lista geral: {valores}')
print(f'Lista de números pares: {valores_par}')
print(f'Lista de números ímpares: {valores_impar}')
