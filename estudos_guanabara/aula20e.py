def contador(*num): #o asterisco significa "desempacotar". Vários parametros que vão ser jogados todos em "num".
    print(num)      #é criado uma TUPLA, onde todos os parametros são empacotados.
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

#programa principal
contador(2, 1 , 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)