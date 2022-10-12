aluno = {}
aluno['nome'] = str(input('Informe o nome do aluno: '))
aluno['media'] = float(input('Informe a média do aluno: '))
print('\n', end='')
if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(f'Nome: {aluno["nome"]}\nMedia: {aluno["media"]}\nSituação: {aluno["situação"]}')
