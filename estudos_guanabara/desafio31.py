distancia = float(input('Digite a distancia da viagem em km: '))
if distancia > 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.50
print(f'O valor total da passagem da viagem é {valor:.2f}')
