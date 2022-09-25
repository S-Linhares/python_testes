soma = 0
velho = 0
media_m = 0
for i in range(0, 4):
    nome = input('Insira o nome: ')
    idade = int(input('Insira a idade: '))
    sexo = input('Informe o sexo(com "m" ou "f"): ')
    media_m = media_m + idade
    if sexo == 'm':
        if velho < idade:
            velho = idade
            aux = nome
    if sexo == 'f' and idade < 20:
        soma = soma + 1
media = media_m // 4
print(f'A media de idade é {media}')
print(f'O homem mais velho é o {aux}')
print(f'Tem {soma} mulheres com menos de 20 anos')
