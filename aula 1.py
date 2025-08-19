# o melhor primeiro programa via console ja visto na humanidade moderna
print('hello world')

# variaveis: não precisam ser declaradas, apenas colocar o nome da variavel e o valor. Exemplos:
# inteiro = 1
# decimal = 1.0
# trueorfalse = True

# definindo variaveis
numero = 1
decimal = 1.0
string = 'palavra'
rapaz = True

# imprimindo variaveis
print(numero)
print(decimal)
print(string)
print(rapaz) 

# imprimindo tipo das variaveis
print(type(numero))
print(type(decimal))
print(type(string))
print(type(rapaz)) 

# convertendo variaveis
numeroconvertido = 1.8
numeroconvertido = int(numeroconvertido)
print(numeroconvertido)
# ou convertendo direto na impressão
outroconvertido = 2.6
print(int(outroconvertido))

# inserindo valores as variaveis (não sei como concatenar)
nome = input('digite seu nome:')
print('seu nome é:'+nome)

# operadores matematicos
# + adição
# - subtração
# * multiplicação
# / divisão mostrando resultados decimais
# // divisão mostrando resultados inteiros
# % resto
# ** potenciação

'''
comentario brabo
que pode pular linhas (brabas)
'''

# Implemente em Python, um algoritmo capaz de calcular a área de um triângulo
base = float(input('digite a base do triângulo: '))
altura = float(input('digite a altura do triângulo: '))
area_triangulo = str((base * altura) / 2)
print('a area do triângulo é '+area_triangulo)