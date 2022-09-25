frase = input('Informe a frase ou palavra: ')
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Essa palavra é um palindromo!')
else:
    print('Essa palavra não é um palindromo!')
