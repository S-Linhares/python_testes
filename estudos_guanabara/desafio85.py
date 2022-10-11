numeros = [[],[]]
for i in range(0, 7):
    num = int(input('Informe o número que deseja: '))
    if (num % 2) == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[1].sort()
numeros[0].sort()
print(60*'=')
print(f'Os números impares são: {numeros[1]}')
print(f'Os números pares são: {numeros[0]}')
