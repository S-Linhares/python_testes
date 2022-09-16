frase = input('Digite a frase: ').strip()
print(f'A quantidade de letras "a" nessa frase é: {frase.lower().count("a")}')
print(f'primeira posição de "a": {frase.lower().find("a")}')
print(f'última posição de "a": {frase.rfind("a")}')
