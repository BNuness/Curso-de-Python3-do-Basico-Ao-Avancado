# vídeo 34. Introdução aos blocos de código + uf/ elif /else (Condicionais)

# if / elif       / else
# se / se não se  / se não

entrada = input('Você que "entrar" ou "sair"? ')

if entrada == 'entrar':    # if + condição (pergunta) | pode ser somente ele
    print('Você entrou no Sistema')
elif entrada == 'sair': # Se não | precisa de um IF
    print('Você saiu do Sistema')
else:                   # Se não | sempre última opção | depende do IF
    print('Você não digitou nem entrar e nem sair')



print('FORA DOS BLOCOS')