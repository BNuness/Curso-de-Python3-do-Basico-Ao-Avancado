# Video 33. Usando a função input para coletar dados do usuário

# input('Qual o seu nome? ') # unção que solicita dados do usuário #joga no Output do VSCode, sendo read only | No caso do coderunning aparece no terminal
# nome = input('Qual o seu nome? ') # coleta  o que foi digitado e coloca na variável nome.
# print(f'O seu nome é {nome=}') #{nome=}
# print(f'O seu nome é {nome=}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero1 = int(numero_1)
int_numero2 = int(numero_2)

print(f'A soma dos números é: {int_numero1 + int_numero2}')