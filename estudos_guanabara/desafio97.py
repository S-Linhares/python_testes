def msg(frase):
    print((len(frase) + 2)*'~')
    print('', frase, '')
    print((len(frase) + 2)*'~')


frase = str(input('Informe uma palavra ou frase: '))
msg(frase)
