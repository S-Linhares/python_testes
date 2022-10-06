total = 0
cont = 0
menor = 0
aux = ''
opcao = ''
while True:
    name = str(input('Digite o nome do produto: '))
    price = float(input('Digite o valor do produto: '))
    total += price
    if price > 1000:
        cont += 1
    if (menor > price) or (menor == 0):
        menor = price
        aux = name
    opcao = str(input('Deseja continuar cadastrando[S/N]? ').upper())
    while (opcao != 'N') and (opcao != 'S'):
        opcao = str(input('Deseja continuar cadastrando[S/N]? ').upper())
    if opcao == 'N':
        print('Saindo de interface de cadastro...')
        break
print(f'O total gasto nesta compra foi: R${total}')
print(f'A quantidade de produtos que custam mais de R$1000 é: {cont}')
print(f'O produto mais barato dessa compra é o(a): {aux}')
