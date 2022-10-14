import time
def contador(ini, fim, passo):
    print(60*'=')
    if ini > fim and passo > 0:
        passo *= -1
    elif ini > fim:
        fim -= 1
    elif ini < fim:
        fim += 1
    elif passo == 0 and ini > fim:
        passo -= 1
    elif passo == 0 and ini < fim:
        passo += 1
    for i in range(ini, fim, passo):
        print(f'{i} ', end='')
        time.sleep(0.25)

print(60 * '=')
print('Contagem de 1 até 10 de 1 em 1')
for i in range(0, 10):
    print(f'{i + 1} ', end='')
    time.sleep(0.25)
print()
print(60 * '=')
print('Contagem de 10 até 0 de 2 em 2')
for i in range(10, -1, -2):
    print(f'{i} ', end='')
    time.sleep(0.25)
print()
print(60 * '=')
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
