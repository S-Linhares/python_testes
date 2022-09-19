import datetime
ano = int(input('Digite o ano que deseja: '))
if ano == 0:
    ano = datetime.date.today().year
if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0)):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
