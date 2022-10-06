num = int(input('Informe um numero n: '))
fibo = 0
cont = 1
ant = 0
aux = 0
while cont < num:
    aux = fibo
    fibo = fibo + ant
    ant = aux
    print(f'{fibo}')
    if fibo == 0:
        fibo += 1
        print(f'{fibo}')
    cont += 1
