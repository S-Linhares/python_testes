inicio = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA:'))
pa = inicio
for i in range(1, 11):
    print(f'{i}º termo: {pa}')
    pa = pa + razao
