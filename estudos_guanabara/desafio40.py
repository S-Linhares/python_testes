n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2
if media >= 7.0:
    print(f'Aprovado! Com média de {media:.2f}')
elif media < 5.0:
    print(f'Reprovado! Com média de {media:.2f}')
else:
    print(f'Recuperação! Com média de {media:.2f}')
