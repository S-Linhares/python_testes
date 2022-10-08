tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Insira o número que deseja entre 0 e 20: '))
    if (num > 20) or (num < 0):
        print('Você digitou um número fora do intervalo. Tente novamente!')
    else:
        print(f'Você digitou o número {tupla[num]}')
        break
