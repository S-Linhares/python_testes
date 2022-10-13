pessoa = {'nome': '', 'sexo': '', 'idade': 0}
pessoas = []
media = 0
mulheres = []
acima_media = []
while True:
    pessoa['nome'] = str(input('Informe o nome da pessoa: '))
    pessoa['sexo'] = str(input('Informe o sexo da pessoa [M/F]: ').upper())
    while pessoa['sexo'] != 'F' and pessoa['sexo'] != 'M':
        print('Opção inválida. Digite uma opção válida!!')
        pessoa['sexo'] = str(input('Informe o sexo da pessoa [M/F]: ').upper())
    pessoa['idade'] = int(input('Informe a idade da pessoa: '))
    media += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy()['nome'])
    pessoas.append(pessoa.copy())
    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())
media /= len(pessoas)
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        acima_media.append(pessoas[i].copy())
print(60*'=')
print(f'O total de pessoas cadastradas foram: {len(pessoas)}')
print(f'A media de idade das pessoas cadastradas é: {media}')
print(f'As mulheres cadastradas foram: ', end='')
for i in range(0, len(mulheres)):
    print(f'{mulheres[i]}... ', end='')
print(f'\nA pessoas que possuem idade acima da média são: ')
for i in acima_media:
    for k, v in i.items():
        print(f'{k}: {v}; ', end='')
    print('\n', end='')
