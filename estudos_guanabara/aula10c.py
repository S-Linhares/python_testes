n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi: {m}')
if m >= 6.0:
    print('Aprovado!')
else:
    print('Reprovado!')
