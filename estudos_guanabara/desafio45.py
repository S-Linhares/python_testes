import random
escolha = int(input('Escolha uma das opções: \n1 - pedra\n2 - papel\n3 - tesoura\n'))
opcoes = ['pedra', 'papel', 'tesoura']
opcao_pc = random.choice(opcoes)
opcao_vc = opcoes[escolha-1]
if escolha == 1:
    if opcao_pc == 'pedra':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nEMPATE!')
    elif opcao_pc == 'papel':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nVOCÊ PERDEU!')
    elif opcao_pc == 'tesoura':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nVOCÊ GANHOU!')
elif escolha == 2:
    if opcao_pc == 'pedra':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nVOCÊ GANHOU!')
    elif opcao_pc == 'papel':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nEMPATE!')
    elif opcao_pc == 'tesoura':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nVOCÊ PERDEU!')
elif escolha == 3:
    if opcao_pc == 'pedra':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nVOCÊ PERDEU!')
    elif opcao_pc == 'papel':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nVOCÊ GANHOU!')
    elif opcao_pc == 'tesoura':
        print(f'Computador: {opcao_pc}!\nVocê: {opcao_vc}!\nEMPATE!')
else:
    print('Você escolheu uma opção inválida!')
