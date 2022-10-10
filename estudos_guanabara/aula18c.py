galera = [['joão', 19], ['ana', 22], ['joaquim', 13], ['maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print('\n', 60*'=', '\n')
for p in galera:
    print(p)
print('\n', 60*'=', '\n')
for p in galera:
    print(p[0])
print('\n', 60*'=', '\n')
for p in galera:
    print(p[1])
print('\n', 60*'=', '\n')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
