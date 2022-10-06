num = 0
result = 0
while True:
    num = int(input('Informe o número que deseja ver a tabuada: '))
    if num < 0:
        print('Encerrando programa...')
        break
    for i in range(1, 11):
        result = num * i
        print(f'{num} x {i:2} = {result}')
