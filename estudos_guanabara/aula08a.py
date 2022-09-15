import math
#from math import sqrt (importa apenas a função "sqrt" de biblioteca math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é: {math.ceil(raiz)}') #ceil arredonda pra cima
print(f'A raiz de {num} é: {math.floor(raiz)}') #ceil arredonda pra baixo
print(f'A raiz de {num} é: {raiz:.3f}')
