inicio = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
pa = inicio
i = 1
j = 10
p = -1
while p != 0:
    print(f'{i:2}º termo: {pa:2}')
    pa = pa + razao
    i += 1
    if i > j:
        p = int(input('Quantos termos a mais deseja ver: '))
        j = j + p
print('FIM!')
