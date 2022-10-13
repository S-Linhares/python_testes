#aposenta após 35 anos de contribuição
import datetime
info = dict()
info['nome'] = str(input('Informe o seu nome: '))
ano = int(input('Informe seu ano de nascimento: '))
info['idade'] = datetime.date.today().year - ano
info['ctps'] = int(input('Informe o número de sua carteira de trabalho (digite "0" caso não possua): '))
if info['ctps'] != 0:
    info['contratação'] = int(input('Informe o ano de contratação: '))
    info['salario'] = float(input('Informe seu salario: '))
    info['aposentadoria'] = info['contratação'] + 35
    print(f'\nNome: {info["nome"]}')
    print(f'Idade: {info["idade"]}')
    print(f'CTPS: {info["ctps"]}')
    print(f'Ano de contratação: {info["contratação"]}')
    print(f'Salario: {info["salario"]}')
    print(f'Ano de aposentadoria: {info["aposentadoria"]}')
else:
    print(f'\nNome: {info["nome"]}')
    print(f'Idade: {info["idade"]}')
    print(f'CTPS: {info["ctps"]}')
