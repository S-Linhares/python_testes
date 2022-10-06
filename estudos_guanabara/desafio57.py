sexo = ''
while (sexo != 'M') and (sexo != 'F'):
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if (sexo != 'M') and (sexo != 'F'):
        print('Sexo digitado inválido, digite novamente.')
print(f'Seu sexo é {sexo.upper()}')
