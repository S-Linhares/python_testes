soma_m = 0
soma_h = 0
mais_18 = 0
opcao = ''
while True:
    sexo = input('Informe o sexo(com "M" ou "F"): ').upper()
    if (sexo != 'M') and (sexo != 'F'):
        print('Sexo inserido inválido!')
    else:
        idade = int(input('Insira a idade: '))
        if sexo == 'M':
            soma_h += 1
        if sexo == 'F' and idade < 20:
            soma_m = soma_m + 1
        if idade >= 18:
            mais_18 += 1
    opcao = str(input('Deseja continuar cadastrando[S/N]? ').upper())
    while (opcao != 'N') and (opcao != 'S'):
        opcao = str(input('Deseja continuar cadastrando[S/N]? ').upper())
    if opcao == 'N':
        print('Saindo de interface de cadastro...')
        break
print(f'O número de pessoas com mais de 18 anos é: {mais_18}')
print(f'A quantidade de homens cadastrados é: {soma_h}')
print(f'Tem {soma_m} mulheres com menos de 20 anos')
