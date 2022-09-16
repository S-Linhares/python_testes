velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80.0:
    multa = (velocidade-80)*7
    print(f'Você foi multado! Com uma multa no valor de R${multa}')
else:
    print('Tudo certo, siga em frente.')
