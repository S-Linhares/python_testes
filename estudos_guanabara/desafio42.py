r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta:'))
r3 = float(input('Informe o comprimento da terceira reta: '))
if (r2-r3) < r1 < (r2 + r3) and (r1-r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('É possivel formar um triangulo equilátero!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('É possivel formar um triangulo escaleno!')
    else:
        print('É possivel formar um triangulo isósceles!')
else:
    print('Não é possivel formar um triangulo!')
