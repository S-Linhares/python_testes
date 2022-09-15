import math
angulo = float(input('Informe o angulo: '))
angulo = math.radians(angulo)
sin = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print(f'O seno é: {sin:.2f}\nO cosseno é: {cos:.2f}\nA tangente é: {tan:.2f}')
