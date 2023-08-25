# Vídeo 46. Fatiamento de strings e a função len

# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [i:f:p] [::] i = inicio, f = fim, p = passo (de quanto em quantos caracteres ele vai pular, padrão 1)
# Obs.: a função len retorna a qtd 
# de caracteres da str
# """
# variavel = 'Olá mundo'
# print(variavel[::-1])

variavel = 'Olá mundo'
# print(variavel[0]) # retorna o caracter no índice indicado

print(variavel[4:]) # Do índice 4 até o fim | inicio 4 e omito o fim por quero que retorne tudo

print(variavel[4:8]) # Do índice 4 até o 7 o índice final não é incluído

print(variavel[0:5]) # Do índice 0 até o 4 (posso omitir o 0) print(variavel[:5])

print(variavel[-8:-2]) # Com índices negativos

print(len(variavel[3])) # mostra a quantidade de caracteres no índice 3

print(len(variavel)) # mostra a quantidade de caracteres da variavel

print(variavel[0:len(variavel):1]) # i = 0, f = 9, p = 1

print(variavel[0:len(variavel):2]) # Passo de 2 em 2

print(variavel[::-1]) # p = -1 inverte a string começa do fim