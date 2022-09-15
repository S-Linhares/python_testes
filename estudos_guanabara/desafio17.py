import math
c1 = float(input('Informe o primeiro cateto: '))
c2 = float(input('Informe o segundo cateto: '))
hipo = math.hypot(c1, c2)
print(f'A hipotenusa é: {hipo:.2f}')
