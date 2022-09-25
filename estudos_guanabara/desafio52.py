numero = int(input('Informe o numero: '))
check = 0
for i in range(2, numero):
    if numero % i == 0:
        check = 1
if check == 0 or numero == 2:
    print(f'{numero} é um número primo!')
else:
    print(f'{numero} não é um numero primo!')
