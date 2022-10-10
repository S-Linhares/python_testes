teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
print(teste)
galera.append(teste)
print(galera)
print('\n', 60*'=', '\n')

#Essas estruturas estão LIGADAS dessa forma. E não feito uma copia. Por falta do fatiamento completo

teste2 = list()
teste2.append('Gustavo')
teste2.append(40)
galera2 = list()
galera2.append(teste2[:])
teste2[0] = 'Maria'
teste2[1] = 22
print(teste2)
galera2.append(teste2[:])
print(galera2)