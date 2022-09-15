#frase[9] mostra a letra na posição selecionada
#frase[9:13] pega todas as letras da posição 9 até a 12. Sendo a chegada na 13 a condição de parada
#frase[9:21:2] pega todas as letras da posição 9 até a 21, mas pulando de 2 em 2 letras
#frase[:5] pega todas as letras da posição 0 até a 5
#frase[15:] pega todas as letras da posição 15 até a última letra
#frase[9::3] pega todas as letras da posição 9 até a última letra, mas pulando de 3 em 3
#len(frase) retorna o comprimento da frase
#frase.count('o') retorna quantas letras 'o' a frase possui (uppercase sensitive)
#frase.count('o',0,13) vai fazer a mesma coisa, mas iniciando a contagem na posição 0 até a 12
#frase.find('deo') vai retornar o intervalo de posição que foi encontrado 'deo'
#frase.fin('android') Se não existir a frase que procura, vai retornar -1
#'curso' in frase -> vai retornar true ou false
#frase.replace('python', 'android') substituiria "python" por "android" na string
#frase.upper() vai transformar todas as letras em maiusculas
#frase.lower() vai transformar todas as letras em minusculas
#frase.capitaliza() vai transformar as letras em minusculas, mas transformar a primeira letra da frase em maiuscula
#frase.title() toda letra antes de espaço em branco fica maiuscula
#frase.strip() remove espaços inuteis, excedentes, no inicio e fim da string
#frase.rstrip() remove espaços inuteis, excedentes, apenas do lado direito(fim)
#frase.lstrip() remove espaços inuteis, excedentes, apenas do lado esquerdo(começo)
#frase.split() vai dividir a string a partir dos espaços vazios
#'-'.join(frase) -> vai juntar a string dividida separando as palavras por '-', ao invés de espaços vazios