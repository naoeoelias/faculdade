# questão 6

ano_atual = int(input('qual o ano atual? '))
ano_nascimento = int(input('qual o seu ano de nascimento? '))
idade = ano_atual - ano_nascimento
print(f'a sua idade é {idade}')

# questão 7

# v = pi * r² * h
raio = float(input('digite o raio do cilindro: '))
altura = float(input('digite a altura do cilindro: '))
volume = 3.14 * raio**2 * altura
print(f'o volume do cilindro é {volume}')

# questão 9

# comentarios e o metodo alternativo, mas usando uma variavel talvez seja mais direto
dias = (int(input('Digite a quantidade de dias: '))) # * 24) * 60) *60 
horas = int(input('Digite a quantidade de horas: ')) # * 60) * 60
minutos = int(input('Digite a quantidade de minutos: ')) # * 60 
segundos = int(input('Digite a quantidade de segundos: '))
segundos_total = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print(f' soma total inputs = {dias+horas+minutos+segundos} segundos total = {segundos_total}')

#teste
num1 = 'elias'
num2 = 'silvestre'
nome = f'{num1} {num2}'
print(f'{nome}')
print((nome+' ')*5)

"""
\n pula linha
\t tab
\r ignora o que ta antes
\' imprime aspa simples
\\ imprime a contra barra

%d ou %i numero inteiro com sinal
%f numero decimal
%o octal
%x hexadecimal
%s string
"""

#teste2
msg1 = 'cuscuz'
msg2 = 'social'
msg3 = 'club'
msg = 'o verdadeiro {} são as amizades feitas no {} numa evolução {}'
print(msg.format(msg1,msg3,msg2))

"""
== igual a
!= diferente de 
< menor que
<= menor ou igual a
> maior que
>= maior ou igual a
"""

#teste3
idade = float(input('digite sua idade: '))
if idade >= 18:
    print('você é maior de idade')
else:
    print('você é menor de idade')
