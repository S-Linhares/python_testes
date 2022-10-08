tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in tupla:
    print(f'Na palavra {i} existem as vogais: ', end='')
    for p in i:
        if p.lower() in 'aeiou':
            print(p.lower(), end=' ')
    print('\n')
