# Vídeo 43. Operadores in e not in

# Operadores in e not in | in = está entre  e not in = não está entre
# Strings são interáveis ()
#   0 1 2 3 4 5 Índices
#   O t á v i o | O no índice 0 e -6 ...
# -6-5-4-3-2-1 Índices Negativos

nome = 'Otávio'
# print(nome[2]) #[Número do índice que quero acessar]
# print(nome[-4]) #[Número do índice que quero acessar]


# print('á' in nome) # Verifica se 'á' está entre as letras do nome retorna True
# print('z' in nome) # Verifica se 'z' está entre as letras do nome retorna False
# print('vio' in nome) # Verifica se 'vio' está entre as letras do nome retorna true
# print('zero' in nome) # Verifica se 'zero está entre as letras do nome retorna False
# print(10 * '-')
# print('á' not in nome) # Verifica se 'á' NÃO está entre as letras do nome retorna False
# print('z' not in nome) 
# print('vio' not in nome) 
# print('zero'not in nome) 


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


