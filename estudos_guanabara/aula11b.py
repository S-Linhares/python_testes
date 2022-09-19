print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!')
cores = {'Limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoBranco': '\033[7:30m'}
nome = 'Samuel'
print(f'{cores["azul"]}{nome} é muito lindo!')
