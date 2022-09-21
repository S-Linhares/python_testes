import datetime
nascimento = int(input('Informe o seu ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento
if idade > 20:
    print('Categoria: Master')
elif idade == 20:
    print('Categoria: Sênior')
elif idade > 14 and idade <=19:
    print('Categoria: Junior')
elif idade > 9 and idade <= 14:
    print('Categoria: Infantil')
elif idade <= 9:
    print('Categoria: Mirim')
