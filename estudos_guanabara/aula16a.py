#tuplas -> ()
#listas -> []
#dicionario -> {}

#Aqui será TUPLAS
#Tuplas são >imutáveis<
#Tuplas podem ser feitas sem o parenteses
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2]) #numeros negativos iniciam no final da tupla, com a contagem sendo iniciado em '-1'
print(lanche[1:3]) #vai até o elemento 3, considerando ele a condição de parada. Ou seja, não o considerando.
print(lanche[:2]) #vai do inicio até o elemento 2
print(lanche[-3:])
print('\n')
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('\n')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('\n')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #O 'ENUMERATE' tem capacidade de mostrar os elementos e as posições
print('\n')
print('Comi pra caramba')
