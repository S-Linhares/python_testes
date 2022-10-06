print('Informe os números que deseja e quando quiser finalizar a inserção de número, insira "999"')
soma = 0
qtd = 0
num = 0
while True:
    num = int(input('Digite o número que deseja inserir: '))
    if num == 999:
        break
    soma = soma + num
    qtd += 1
print(f'Soma de todos os números inseridos: {soma}')
print(f'Quantidade de números inseridos: {qtd}')