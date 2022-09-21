preco = float(input('Informe o preço do produto: '))
pagamento = int(input('Escolha a forma de pagamento: \n1 - Dinheiro/À vista\n2 - À vista no cartão\n'
                      '3 - Em até 2x no cartão\n4 - 3x ou mais no cartão\n'))
if pagamento == 1:
    total = preco - (preco * 0.10)
    print(f'Total a pagar com 10% de desconto: {total}')
elif pagamento == 2:
    total = preco - (preco * 0.05)
    print(f'Total a apgar com 5% de desconto: {total}')
elif pagamento == 3:
    print(f'Total a pagar sem desconto: {preco}')
elif pagamento == 4:
    total = preco + (preco * 0.20)
    print(f'Total a pagar com 20% de juros: {total}')
else:
    print('Opção escolhida inválida')
