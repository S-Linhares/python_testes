algo = input('Digite algo: ')
print(f"Foi digitado: {algo}")
print(f"{algo} é do tipo: {type(algo)}")
print(f"{algo} é numerico? {algo.isnumeric()}")
print(f"{algo} é alfabetico? {algo.isalpha()}")
print(f"{algo} é alfanumerico? {algo.isalnum()}")
print(f"{algo} só tem espaços? {algo.isspace()}")
print(f"{algo} possui todas as letras maiusculas? {algo.isupper()}")
print(f"{algo} possui todas as letras minusculas? {algo.islower()}")
print(f"{algo} está capitalizada? {algo.istitle()}") #capitalizada é a mistura de maiuscula e minuscula