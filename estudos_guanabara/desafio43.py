import math
altura = float(input('Informe a sua altura em metros: '))
peso = float(input('Informe o seu peso em kg:'))
imc = peso/(math.pow(altura, 2))
if imc > 40:
    print('Você está com obesidade morbida')
elif imc <= 40 and imc > 30:
    print('Você está com obesidade')
elif imc <= 30 and imc > 25:
    print('Você está com sobrepeso')
elif imc <= 25 and imc > 18.5:
    print('Você está na faixa de peso ideal')
else:
    print('Você está abaixo do peso')
