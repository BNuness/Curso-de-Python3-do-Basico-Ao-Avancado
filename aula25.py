# Vìdeo 44.Intepolação de string com % em python

"""
Interpolação básica de strings
Place holder
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789) x= gera Hexadecimal minúsculo | X  = gera maiúsculo
"""
nome = 'Bruno'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' %(nome,preco) #%tipo , %(variaveis) caso seja uma não precisa de ()
print(variavel)
print('O hexadecimal de %d é %04x' %(15, 15))  # Hexadecimal de 15  %04 completa com 4 zeros