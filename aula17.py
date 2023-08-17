# Vídeo 35. if, elif e else: entendendo o fluxo do interpretador em condicionais

# if / elif       / else  #else ultima coisa a ser executada | 1 if e um else no bloco inteiro | posso utilizqaar quantos elif eu quiser
# se / se não se  / se não


condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
    #pass #pass | para não escrever o código  no momento ... ou pass
elif condicao3:
    print('Código para condição 3')     
elif condicao4:
    print('Código para condição 4')

else:
    print('Nenhuma condição foi satisfeita.')

# Quando encontra uma condição verdadeira sai do bloco | sempre executa a primeira verdadeira e ignora o resto

if 10 == 10:
    print('Outro if')

print('Fora do if')


# if condicao1:
#     print('Este é o código do if')
# else:
#     print('Este é o else do primeiro if')

# if 10 == 10:
#     print('Outro if')

# print('Fora do if')
