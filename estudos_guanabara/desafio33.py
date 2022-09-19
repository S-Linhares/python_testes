n1 = float(input('Informe o primeiro numero: '))
n2 = float(input('Informe o segundo numero: '))
n3 = float(input('Informe o terceiro numero: '))
if (n1 > n2) and (n1 > n3):
    print(f'O maior número é {n1}')
else:
    if (n2 > n1) and (n2 > n3):
        print(f'O maior número é {n2}')
    else:
        print(f'O maior número é {n3}')
