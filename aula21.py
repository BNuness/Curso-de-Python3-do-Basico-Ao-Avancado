# Vídeo 40. Operador Lógico "and"

# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada como false e será avilada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor (Valor não existe)

# Só para entender a lógica não é para ser utilizado
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# # if condicao: só será executado se o resultado for true
# #   ...
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entre')
# else:
#     print('Sair')

# Avaliação de curto-circuito
# Se ele chega em um valor false, não checa mais nada
print(True and True and True)
print(True and False and True)
print(bool(0))
print(True and 0 and True) # Dependendo do que a condição retornar ele pode parar na posição e retornar o valor da condição


if 1 and 1:
    print(True and 1 and False)


