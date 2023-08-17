# Vídeo 38. Exercício de programação com if e comparação

# Utilizando os operadores de comparação maior e menor, utilizar if, elif e else
# o valor que for maior aparecer primeiro

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# if primeiro_valor > segundo_valor:
#     print(f'primeiro_valor={primeiro_valor} é maior que segundo valor={segundo_valor}')
# elif segundo_valor > primeiro_valor:
#     print(f'segundo_valor={segundo_valor} é maior que primeiro_valor={primeiro_valor}')
# else:
#     print(f'primeiro_valor={primeiro_valor} e segundo valor={segundo_valor} são iguais')


if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior que ={primeiro_valor=}')
else:
    print(f'{primeiro_valor=} e {segundo_valor=} são iguais')


'''
Solução Professor:
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
'''