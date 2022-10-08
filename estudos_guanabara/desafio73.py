tupla = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
         'América-MG', 'Botafogo', 'São Paulo', 'Fortaleza', 'Bragantino', 'Goiás', 'Santos', 'Ceará-SC', 'Coritiba',
         'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')

print('Os primeiros 5 colocados são: ')
for i in range(0, 5):
    print(f'{i+1} - {tupla[i]}')
print('\n')

print('Os últimos 4 colocados são: ')
for i in range((len(tupla) - 4), len(tupla)):
    print(f'{i+1} - {tupla[i]}')
print('\n')

print('Os times em ordem alfabetica ficam: ')
for i in range(0, len(tupla)):
    print(f'{i+1} - {sorted(tupla)[i]}')
print('\n')

for i in range(0, len(tupla)):
    if(tupla[i] == 'Chapecoense'):
        print(f'Chapecoense se encontra na posição {i+1} da tabela')
        break
    elif (tupla[i] != 'Chapecoense') and (i == (len(tupla) - 1)):
        print('Chapecoense não se encontra na tabela da serie A. :(')
