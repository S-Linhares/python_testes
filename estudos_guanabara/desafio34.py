salario = float(input('Informe o salario do funcionario: '))
if salario > 1250.00:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print(f'O seu novo salario é {aumento:.2f}')
