#Dicionarios = {}
#declarando: dados = dict() ; dados = {} ; dados = {'nome': 'Pedro', 'idade': 25}
#printando: print(dados['nome']) = pedro ; print(dados['idade']) = 25
#Inserindo dados: dados['sexo'] = 'M'
#removendo dados: del dados['idade']
#print(exemplo.values()): retorna todos os dados do dicionario
#print(exemplo.keys()): retorna todos os identificadores do dicionario
#print(exemplo.items()): retorna todos os dados e identificadores do dicionario

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(30*'=', '\n')

for k in pessoas.keys():
    print(k)
print('\n')
for k in pessoas.values():
    print(k)
print('\n')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n')
pessoas['nome'] = 'leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n')
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n')
