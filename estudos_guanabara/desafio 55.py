maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Informe o peso: '))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif maior < peso:
        maior = peso
    elif menor > peso:
        menor = peso
    elif peso < 0:
        print('Peso informado inválido')
print(f'O maior peso informado foi {maior}\nO menor peso informado foi {menor}')
