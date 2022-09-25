maior = 0
menor = 0
for i in range(0, 7):
    ano = int(input('Informe o ano de nascimento: '))
    if 2022 - ano >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores de idade!')
