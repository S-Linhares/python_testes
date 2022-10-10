pilha = []
frase = str(input('Informe a expressão: '))
for i in range(0, len(frase)):
    if frase[i] == '(':
        pilha.append('(')
    elif frase[i] == ')':
        pilha.pop()
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')