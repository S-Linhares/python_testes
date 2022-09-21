import datetime
nascimento = int(input('Informe o seu ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento
passou = idade - 18
falta = 18 - idade
if idade == 18:
    print('Este é o ano que você deve se alistar!')
elif idade < 18:
    print(f'Não chegou o momento de você se alistar! Falta {falta} ano(s)')
else:
    print(f'Já faz {passou} ano(s) que passou da sua época de se alistar!')
