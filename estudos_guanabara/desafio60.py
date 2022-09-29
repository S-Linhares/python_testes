num = int(input('Digite o número que deseja: '))
fatorial = num - 1
while fatorial > 1:
    num = num * fatorial
    fatorial -= 1
print(f'O fatorial é {num}')
