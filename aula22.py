# vídeo 41. Operador Lógico 'or'

# Operadores lógicos
# and (e) or (ou) not (não)
# or  - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor.


# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: #Avalia a condição entre () primeiro e inteira
#     print('Entrar')
# else:
#     print('Sair')


# Avaliação de curto circuito
# print(True and 0 and True)

# print(True and 0 and True) # vai avaliar como True

# print(0 or False or 0 or 'abc') # retorna o ultimo valor considerado verdadeiro que foi o abc | na primeira vez que ele encontrar um valor verdadeiro ele vai retorná-lo

# senha = (0 or False or 0 or 'abc')
# print(senha)

senha = input('Senha: ') or 'Sem senha'
print(senha)