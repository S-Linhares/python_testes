import random
tupla = (random.randint(0, 1001), random.randint(0, 1001), random.randint(0, 1001), random.randint(0, 1001),
         random.randint(0, 1001))
print(f'Valores sorteados: {tupla}')
print(f'O maior número da lista é {max(tupla)}')
print(f'O menor número da lista é {min(tupla)}')
