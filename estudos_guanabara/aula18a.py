dados = list()
pessoas = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas.append(dados[:]) #o dois pontos sem indicar inicio e fim quer dizer um fatiamento completo. Pegando tudo.
pessoas2 = [['pedro', 25], ['maria', 19], ['joão', 32]]
print(pessoas2[0][0])
print(pessoas2[1][1])
print(pessoas2[2][0])
print(pessoas2[1])
