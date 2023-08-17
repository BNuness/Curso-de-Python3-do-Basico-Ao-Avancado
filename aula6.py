# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool tipos imutaveis e primitivos / literais
print(1 + 1)
print('a' + 'b')
print('1', type('1'))
print(int('1'), type(int('1'))) #converte str em int
print(int('1') + 1)
print(float('1') + 1) #quando combino float com inteiro me retorna outro float
print(type(float('1') + 1)) #Executa de dentro pra fora
print(bool('')) #String vazia é considerada false e uma com valor mesmo sendo espaço é true
print(str(11) + 'b')

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

#dinamica e forte(Python não consegue concatenar int com str por exemplo) só coneverte um tipo em outro se isso puder ser feito
#fraca normalmente converte um tipo em outro