print('>>> ESTUDO DIRIGIDO 1 <<<')

# 1. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

a1 = int(input('digite o primeiro numero inteiro:\n')) # recebe o 1º valor
a2 = int(input('digite o segundo numero inteiro:\n')) # recebe o 2º valor
print(f'a soma dos numeros {a1} e {a2} é: {a1 + a2}') # printa os valores e faz o calculo no proprio print
print('1ex1 ^^^\n')

# 2. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

b2 = float(input('digite um valor em metros:\n')) # recebe o valor em metros
print(f'o valor de {b2} metros em milimetros é {b2 * 1000}') # printa os valores, fazendo o calculo no proprio print
print('1ex2 ^^^\n')

# 3. Escreva um programa que calcule um aumento de 15% para um salário de R$ 750.

c1 = 750 + (750 * 15 / 100) # ou * 0.15 // faz o calculo
print(f'o resultado do aumento de 15% em cima do valor 750 é de: {c1}') # printa os valores
print('1ex3 ^^^\n')

# 4. Elabore um programa que realize a conversão do valor em dólares para real. (Considere a cotação: 1 dólar americano = 4,96 reais)

d1 = float(input('digite o valor em dolares:\n')) # recebe valor em dolares
conversao = d1 * 4.96 # faz a conversão
print(f'o valor em dolares ({d1}) convertido em reais é R${conversao}') # printa os valores
print('1ex4 ^^^\n')

# 5. Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é: F = (9 * c / 5) + 32.

e1 = float(input('digite o valor em celsius para ser convertido em fahrenheit:\n')) # recebe graus celsius para conversão
e2 = (9 * e1 / 5) + 32 # faz a conversão
print(f'a conversão de ºC ({e1}) para ºF é: {e2}')
print('1ex5 ^^^\n')

# 6. Elabore um programa que solicite o ano em que você nasceu. Crie uma mensagem que inclua o ano e informe quantos anos você tem atualmente.

f1 = int(input('digite o ano que você nasceu:\n')) # recebe o ano de nascimento
f2 = int(input('digite o ano atual:\n')) # recebe o ano atual
print(f'você está no ano de {f2} e possui {f2-f1} anos.') # printa o ano que você está e a sua idade atual.
print('1ex6 ^^^\n')

# 7. Faça um programa que calcule o volume de um cilindro, dado pela fórmula V = π. r^2. h. Solicite ao usuário o raio da base e a altura do cilindro.

g1 = float(input('digite o raio da base:\n')) # recebe o raio da base do cilindro
g2 = float(input('digite a altura do cilindro:\n')) # recebe a altura do cilindro
g3 = 3.14 * g1 ** 2 * g2 # calcula o volume do cilindro
print(f'o volume do cilindro, dado o raio {g1} e a altura {g2} resulta {g3}') # printa todos os valores, os recebidos e os calculados.
print('1ex7 ^^^\n')

# 8. Escreva um programa que calcule o faturamento de um representante comercial que recebe R$ 500,00 fixos e 6% de comissão sobre as vendas do mês.
# Considere que ele fechou o mês com um valor de R$ 12.398,00 em vendas. Exiba o resultado com duas casas decimais.

h1 = 500.00 # salario fixo
h2 = 12398.00 # vendas mensal
h3 = 0.06 # comissão de 6%
h4 = h1 + (h2 * h3) # calculo do faturamento
print(f'o faturamento do funcionario foi de {h4:.2f}') # printa o valor do faturamento com duas casas decimais.
print('1ex8 ^^^\n')

# 9. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

i1 = int(input('digite a quantidade de dias:\n')) * 86400 # converte direto de dias para segundos
i2 = int(input('digite a quantidade de horas:\n')) * 3600 # converte direto de horas para segundos
i3 = int(input('digite a quantidade de minutos:\n')) * 60 # converte direto de minutos para segundos
i4 = int(input('digite a quantidade de segundos:\n')) # aqui não precisa de conversão
i5 = i1 + i2 + i3 + i4 # calcula a soma de tudo
print(f'a soma de tudo citado anteriormente em segundos é de: {i5}') # printa a soma de tudo
print('1ex9 ^^^\n')

# FIM ESTUDO DIRIGIDO 1

print('>>> ESTUDO DIRIGIDO 2 <<<')

# 1. Faça um programa que solicite a situação de um usuário e o informe se tem direito de utilizar a fila de prioridade.

z1 = int(input('[1] situação 1\n[2] situação 2\n[3] situação 3\ndigite a sua situação:\n')) # printa as situações, solicitando um input
z2 = 'você tem direito a usar a fila de prioridade' # so pra poupar tempo
# o if abaixo verifica a situação, e exibe se o usuario tem ou não tem direito a fila de prioridade
if z1 == 1:
    print(z2)
elif z1 == 2:
    print(z2)
elif z1 == 3:
    print(z2)
else:
    print('você não tem direito a utilizar a fila de prioridade.')
print('2ex1 ^^^\n')

# 2. Faça um algoritmo que leia três números inteiros e que informe qual o maior deles.

x1 = int(input('digite o primeiro numero inteiro:\n'))
x2 = int(input('digite o segundo numero inteiro:\n'))
x3 = int(input('digite o terceiro numero inteiro:\n'))

if x1 > x2 and x1 > x3:
    print(f'{x1} é o maior numero. sendo maior que: {x2} e {x3}')
elif x2 > x1 and x2 > x3:
    print(f'{x2} é o maior numero. sendo maior que: {x1} e {x3}')
elif x3 > x1 and x3 > x2:
    print(f'{x3} é o maior numero. sendo maior que: {x1} e {x2}')
else:
    print('operação invalida')
print('2ex2 ^^^\n')

'''
3. Crie um programa para calcular o preço final a partir do número de camisas. As seguintes
regras foram definidas para aplicar um desconto:
▪ Até 5 camisas, desconto de 3%
▪ Acima de 5 camisas e até 10 camisas, desconto de 5%; e
▪ Acima de 10 camisas, desconto de 7%
Imprima o valor a ser pago pelo cliente, sabendo que o preço da camisa é R$ 12,50.
'''
numero_camisas = int(input('Informe o numero de camisas: '))
preco_total = 12.50 * numero_camisas

if (numero_camisas >= 0) and (numero_camisas <= 5):
    preco_final = preco_total - 0.03 * preco_total
    print(f'Com o desconto de 3%, o preço a ser pago é R${preco_final}')
elif (numero_camisas >= 0) and (numero_camisas <= 10):
    preco_final = preco_total - 0.05 * preco_total
    print(f'Com o desconto de 5%, o preço a ser pago é R${preco_final}')
elif (numero_camisas > 10):
    preco_final = preco_total - 0.07 * preco_total
    print(f'Com o desconto de 7%, o preço a ser pago é R${preco_final}')
else:
    print('Dado Invalido, insira um valor positivo para o numero de camisas')
print('2ex3 ^^^\n')

'''
4. Construa um programa que valide o acesso de um usuário ao sistema. Caso o par
usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem
vindo!”. Caso contrário, “Usuário e senha não conferem”.
'''
usuario = input('digite o seu usuario: ')
senha = input('digite a sua senha: ')

log_user = 'elias'
log_pass = 'cuscuz'

if (usuario == log_user) and (senha == log_pass):
    print(f'Bem Vindo {usuario}!')
else:
    print('Usuario e/ou senha não conferem.')
print('2ex4 ^^^\n')

'''
5. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse
80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor
da multa, cobrando R$ 5 por km acima de 80 km/h.
'''
vel_veiculo = float(input('Digite a velocidade do veiculo: '))

if vel_veiculo > 80:
    valor_multa = (vel_veiculo - 80) * 5
    print(f'Você foi multado em R${valor_multa}.')
else:
    print('Você não foi multado')
print('2ex5 ^^^\n')

'''
6. Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e
R$ 0,45 para viagens mais longas.
'''
distancia_percorrida = float(input('Digite a Distancia que será Percorrida: '))

if (distancia_percorrida >= 0) and (distancia_percorrida <= 200):
    valor_pago = 0.5 * distancia_percorrida
else:
    valor_pago = 0.45 * distancia_percorrida

print(f'o valor a ser pago vai ser de {valor_pago} reais.')
print('2ex6 ^^^\n')

'''
7. Escreva um programa que leia dois números e que pergunte qual operação você deseja
realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada.
'''
num1 = float(input('digite o primeiro numero: '))
num2 = float(input('digite o segundo numero: '))
op = int(input('[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\nDigite a operação a ser feita: '))

if op == 1:
    operacao = 'soma'
    resultado = num1 + num2
elif op == 2:
    operacao = 'subtração'
    resultado = num1 - num2
elif op == 3:
    operacao = 'multiplicação'
    resultado = num1 * num2
elif op == 4:
    operacao = 'divisão'
    resultado = num1 / num2

print(f'o resultado da {operacao} é {resultado}')
print('2ex7 ^^^\n')

'''
8. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O
programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a
pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor
da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
'''
valor_casa = float(input('digite o valor da casa a comprar: '))
valor_salario = float(input('digite o valor do seu salario: '))
qtd_meses = int(input('digite a quantidade de anos a pagar: ')) * 12
prestacao = valor_casa / qtd_meses

if prestacao > valor_salario * 0.30:
    print('emprestimo bancario não aprovado')
else:
    print('emprestimo bancario aprovado')
print('2ex8 ^^^\n')

'''
9. Crie um programa que solicite do usuário a resposta para três perguntas que sejam de
múltipla escolha. Cada pergunta terá uma alternativa correta e, ao final, mostre quantas
questões o usuário acertou e quantos pontos obteve, sabendo que uma questão correta
equivale a dois pontos.
'''
qtd_acertos = 0

p1 = int(input('[1] São Paulo\n[2] Brasilia\n[3] Rio de Janeiro\n[4] Salvador\nQual é a capital do Brasil? '))
if p1 == 2:
    qtd_acertos += 1
p2 = int(input('[1] Jacaré\n[2] Gato\n[3] Galinha\n[4] Sapo\nQual desses animais é um mamífero? '))
if p2 == 2:
    qtd_acertos += 1
p3 = int(input('[1] Verde\n[2] Laranja\n[3] Azul\n[4] Roxo\nQual dessas cores é primária? '))
if p3 == 3:
    qtd_acertos +=1
print(f'a quantidade de acertos é: {qtd_acertos}.\na quantidade de pontos é: {2 * qtd_acertos}.')
print('2ex9 ^^^\n')
print('FIM')