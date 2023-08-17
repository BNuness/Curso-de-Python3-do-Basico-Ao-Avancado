# Introdução a formatação de string
# Aula 31. Uma introdução às f-strings(formatação de strings) | esse f significa formatação

nome = 'Bruno Nunes'
altura = 1.79
peso = 79
# imc = peso / altura ** 2 precedência
imc = peso / (altura ** 2) # IMC = peso / (altura x altura) ... Ellipsis e não gera erro (place holder) para escrever código dps


linha_1 = f'{nome} tem {altura:.2f} de altura,' # f: permite introduzir variáveis em texto | {} introduzir as variáveis | :.2f 2 casas decimais (:,.2f vírgula e ponto)
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é '
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)


#print(nome, 'tem', altura, 'de altura, pesa', peso,'quilos e seu IMC é: ', imc)