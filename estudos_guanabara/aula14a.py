c = 1
n = 1
r = 's'
while c < 10:
    print(c)
    c += 1
while n != 0:
    n = int(input('Digite um valor (DIGITE 0 PARA SAIR): '))
print('Fim')
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).lower()
print('Fim')
