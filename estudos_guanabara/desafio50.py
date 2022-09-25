lista = []
soma = 0
for i in range(0, 6):
    lista.append(int(input('Informe o número que deseja incluir na lista: ')))

for i in range(0, 6):
    if lista[i] % 2 == 0:
        soma = soma + lista[i]
print(f'A soma dos pares é: {soma}')
