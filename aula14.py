# Vídeo 32. Formatação de strings com método format
# tudo em python é um objeto, objetos geralmente têm métodos dentro deles, objetos tem ações ele pode fazer algumas ações (métodos)


a = 'A'
b = 'B'
c = 1.1

#string = 'a={0} b={1} c={2:.2f}' # 0,1 e 2 índices, nessa forma não dependo da ordem
#formato = string.format(a, b, c) # na ordem {} traz os argumentos da função format no caso a variável a. parâmetro nomeado, é quando eu dou nome paras coisas dentor da chamada ou criação das funções


string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1 = a, nome2 = b, nome3 = c   # tudo que vir depois do parâmetro nomeado precisa ser nomeado | nome1 = parâmetro a  = argumento
    
    )


print(formato)



# Quando uma função está dentro de um objeto esta função é chamada de método