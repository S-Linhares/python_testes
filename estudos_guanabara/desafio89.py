boletim = [[], [], []]
while True:
    boletim[0].append(str(input('Nome do aluno: ')))
    boletim[1].append(float(input('1º nota: ')))
    boletim[2].append(float(input('2º nota: ')))
    opcao = str(input('Deseja continuar [S/N]?').upper())
    if opcao == 'N':
        break
    while opcao != 'N' and opcao != 'S':
        print('Opção inválida. Digite uma opção válida!!')
        opcao = str(input('Deseja continuar [S/N]?').upper())
print(30*'=')
print('\t\tBOLETIM GERAL')
print(30*'=')
print('Nº\tNome\t\tMédia')
print(30*'-')
for i in range(0, len(boletim[0])):
    media = (boletim[1][i] + boletim[2][i])/2
    print(f'{i}\t{boletim[0][i]}\t\t{media}')
print(30*'-')

while True:
    option = int(input('Mostrar notas de qual aluno [999 interrompe]? '))
    if option == 999:
        print('Finalizando programa...')
        break
    print(f'Aluno: {boletim[0][option]}')
    print(f'Nota 1: {boletim[1][option]}')
    print(f'Nota 2: {boletim[2][option]}')
    print(30*'-')
