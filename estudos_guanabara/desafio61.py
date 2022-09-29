inicio = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
pa = inicio
i = 1
while i <= 10:
    print(f'{i}º termo: {pa}')
    pa = pa + razao
    i += 1
