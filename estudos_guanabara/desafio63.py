num = int(input('Informe um numero n: '))
fibo = 0
cont = 1
ant = 0
while cont <= num:
    fibo = fibo + ant
    print(f'{fibo}')
    ant = fibo
    if fibo == 0:
        fibo += 1
    cont += 1
