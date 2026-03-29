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
