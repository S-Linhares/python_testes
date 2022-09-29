sexo = ''
while (sexo != 'M') and (sexo != 'F'):
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
print(f'Seu sexo é {sexo.upper()}')
