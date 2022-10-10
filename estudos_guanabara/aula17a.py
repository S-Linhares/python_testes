#Listas são mútaveis

#Definição de lista é com '[]' colchetes

#Adicionar item ao final da lista: exemplo.append('item novo')

#Adicionar item em local especifico da lista: exemplo.insert(posição, 'item novo')

#Deletar item da lista: del exemplo[posição] ; exemplo.pop(posição) ; exemplo.remove('nome item')

#Estrutura de verificação de item estar incluso na lista: if 'nome item' in exemplo:

#Formas de declarar uma lista: valores = list(range(4, 11)). Vai criar uma lista com números de 4 até 10, sendo uma
#lista de 6 posições;
#valores = [1, 2, 3, 4, 5, 6]

#Estrutura de organização crescente: exemplo.sort() ; descrescente: exemplo.sort(reverse = True)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')
