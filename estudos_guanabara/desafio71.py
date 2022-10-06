valor = int(input('Informe o valor que deseja sacar: '))
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0
while True:
    while valor - 50 >= 0:
        cont_50 += 1
        valor = valor - 50
    while valor - 20 >= 0:
        cont_20 += 1
        valor = valor - 20
    while valor - 10 >= 0:
        cont_10 += 1
        valor = valor - 10
    while valor - 1 >= 0:
        cont_1 += 1
        valor = valor - 1
    if valor == 0:
        break
print('Para este saque, serão utilizadas: ')
print(f'{cont_50:2} cédulas de R$50')
print(f'{cont_20:2} cédulas de R$20')
print(f'{cont_10:2} cédulas de R$10')
print(f'{cont_1:2} cédulas de R$1')
