lista_a = []
lista_f = []
frase = str(input('Informe a expressão: '))
for i in range(0, len(frase)):
    if frase[i] == '(':
        lista_a.append(frase[i])
    elif frase[i] == ')':
        lista_f.append(frase[i])
if len(lista_a) == len((lista_f)):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
