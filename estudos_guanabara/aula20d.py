def contador(*num): #o asterisco significa "desempacotar". Vários parametros que vão ser jogados todos em "num".
    print(num)      #é criado uma TUPLA, onde todos os parametros são empacotados.
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim!')

#programa principal
contador(2, 1 , 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)