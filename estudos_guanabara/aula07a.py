#adição "+"
#subtração "-"
#multiplicação "*"
#divisão "/"
#potencia "**", "pow(base, potencia)"
#raiz quadrada "raiz**(1/2)"
#raiz cubica "raiz**(1/3)"
#divisão inteira "//"
#resto da divisão "%"
#ordem de precedência:
#1: "()"
#2: "**"
#3: "*", "/", "//", "%"
#4: "+", "-"

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira um segundo numero: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1/n2
pot = n1**n2
raiz = soma**(1/2)
div_int = n1//n2
resto = n1%n2
print('A soma é: {}\nA subtração é: {}\nA multiplicação é: {}\nA divisão é: {:.2f}\n'
      'A potencia é: {}\nA raiz quadrada é: {:.3f}\nA divisão inteira é: {}\nO resto da divisão é: {}\n'
      ''.format(soma, sub, mult, div, pot, raiz, div_int, resto))
