# 1. (n + n)  () de dentro pra fora
# 2. **
# 3. * / // % Serão executadas da esquerda para direita se os operadores tiverem a mesma precedência
# 4. + -

# conta_1 = 1 + 1 ** 5 + 5 
# print(conta_1)


conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)