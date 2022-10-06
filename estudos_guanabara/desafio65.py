cond = 's'
total = 0
qtd = 0
maior = 0
menor = 0
while cond == 's':
    num = int(input('Informe o número que deseja incluir: '))
    total = total + num
    qtd += 1
    if num > maior or maior == 0:
        maior = num
    if num < menor or menor == 0:
        menor = num
    cond = str(input('Deseja inserir mais um número[s/n]? ').lower())
media = total/qtd
print(f'A média dos valores é:{media}\nO maior número é:{maior}\nO menor número é:{menor}\n')
