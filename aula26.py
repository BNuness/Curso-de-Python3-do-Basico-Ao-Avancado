#Vídeo 45. Formatação de strings com f-strings

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')

# padding básicamente colocalargura fixa da variavel caso ela não alcance a largura fixa colocada 
#: >10 preenche com dez caracteres de ponto a esquerda contando com a variavel
print(f'{variavel:.>10}')

# <10 dez caracteres de ponto a direita 
print(f'{variavel:.<10}.')

# no centro
print(f'{variavel:.^10}.')

# 1 casa decimal
print(f'{1000.4873648123746:.1f}')

# Separa a milhar por , e 1 casa decimal
print(f'{1000.4873648123746:,.1f}')

# Adiciona o sinal de positivo, separa a milhar por ',' e 1 casa decimal
print(f'{1000.4873648123746:+,.1f}')

# 0= Força o númeora a aparecer depois do zero , adiciona o sinal de positivo, separa a milhar por ',' e 1 casa decimal
print(f'{1000.4873648123746:0=+10,.1f}')

# Mostra o hexadecimal de 1500 preenchenco com zero
print(f'O hexadecimal de 1500 é {1500:08x}')

# !r Chama o método repr
print(f'{variavel!r}')
