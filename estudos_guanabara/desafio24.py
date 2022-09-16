city = input('Informe o nome da cidade: ')
city = city.split()
vf = 'SANTO' in city[0].upper()
print(f'Começa com SANTO no nome: {vf}')
