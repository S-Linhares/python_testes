valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do seu salario: '))
anos = int(input('Informe em quantos anos deseja parcelar: '))
meses = anos * 12;
prestacao = valor_casa/meses
excesso = salario * 0.30
if prestacao > excesso:
    print('Emprestimo negado!!!!!\nSua parcela mensal excede 30% de seu salario')
else:
    print('Emprestimo concedido!!!!')
