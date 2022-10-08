tupla = (int(input('Informe o 1º valor que deseja adicionar: ')),
         int(input('Informe o 2º valor que deseja adicionar: ')),
         int(input('Informe o 3º valor que deseja adicionar: ')),
         int(input('Informe o 4º valor que deseja adicionar: ')))

print(f'O valor 9 apareceu um total de {tupla.count(9)} vezes nesta tupla')
if 3 in tupla:
    print(f'A primeira aparição do número 3 na tupla é na posição {tupla.index(3) + 1}')
else:
    print('Não existe número 3 nesta tupla')
print('Os números pares são:', end='')
for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        print(f' {tupla[i]}', end=' ')
