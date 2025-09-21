

'''1. Faça um programa que exiba os números de 1 a 100.'''
cont = 1
print(cont)

while cont <= 100:
    print(cont)
    cont += 1
    
print('3ex1 ^^^\n')

'''2. Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O
programa deve imprimir 10, 9, 8, ... , 1, O e Fogo! na tela.'''

import time

t = 1
while t <= 10:
    time.sleep(1)
    print(t)
    t += 1
else:
    print('Fogo!')

print('3ex2 ^^^\n')

'''3. Peça ao usuário para inserir uma senha até que ela contenha pelo menos 8 caracteres.'''

senha = input('digite uma senha com 8 caracteres: ')

while len(senha) < 8:
    senha = input('digite uma nova senha que contenha 8 caracteres: ')
else:
    print('operação concluida.')

print('3ex3 ^^^\n')

'''4. Peça ao usuário para inserir números inteiros até que ele insira um número negativo.
Calcule e imprima a soma apenas dos números pares inseridos.'''

numero = 0
soma_pares = 0
contador = 1

while numero >= 0:
    numero = int(input(f'{contador}. digite um numero inteiro positivo: '))
    contador += 1
    if (numero % 2) == 0 and (numero > 0):
        soma_pares += numero
    if contador > 10:
        break

print(f'o valor da soma de todos os pares digitados é: {soma_pares}.')

print('3ex4 ^^^\n')

'''5. Crie um jogo em que o computador escolhe um número aleatório entre 1 e 100, e o
jogador tem que adivinhar o número. Permita que o jogador continue adivinhando até
acertar o número.'''

import random

numero_sorteado = random.randint(1,10)
numero_escolhido = int(input('digite um numero inteiro: '))
tentativas = 1


while numero_escolhido != numero_sorteado:
    numero_escolhido = int(input('digite outro numero inteiro: '))
    tentativas += 1

print(f'parabens, {numero_sorteado} foi o numero sorteado. você acertou com {tentativas} tentativas.')

print('3ex5 ^^^\n')

'''6. Escreva um algoritmo que solicite ao usuário o primeiro termo, a razão e o número de
termos de uma progressão aritmética. Imprima os termos da progressão.'''

primeiro_termo = int(input('informe o 1° termo da pa: '))
razao = int(input('informe a razão da pa: '))
numero_termos = int(input('informe o numero de termos da pa: '))
contador3 = 1 
termo_anterior = primeiro_termo
print(f'o {contador3}° termo da pa é: {primeiro_termo}.')

while contador3 < numero_termos:
    proximo_termo = termo_anterior + razao
    termo_anterior = proximo_termo
    contador3 += 1
    print(f'o {contador3}° termo da pa é: {proximo_termo}.')

print('3ex6 ^^^\n')

'''7. Crie um programa de caixa eletrônico simples que permita ao usuário verificar o saldo,
fazer depósitos e saques.'''

saldo = 0

operacao = int(input('Digite a operação desejada:\n[1] Verificar Saldo\n[2] Fazer Deposito\n[3] Fazer Saque\noperação: '))

if operacao == 1:
    print(f'O seu saldo é de: R${saldo}')
elif operacao == 2:
    saldo += float(input('digite o valor a ser depositado: '))
    print(f'O seu saldo é de: R${saldo}')
elif operacao == 3:
    saldo -= float(input('digite o valor do saque: '))
    print(f'O seu saldo é de: R${saldo}')
else:
    print('operação invalida!')

print('3ex7 ^^^\n')

'''8. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros
no período.'''

deposito_inicial = float(input('digite o valor inicial que sera depositado na poupança: '))
taxa_juros = float(input('digite a taxa de juros da aplicação: ')) / 100
contador2 = 1

while contador2 <= 24:
    montante = deposito_inicial * (1 + taxa_juros)** contador2
    print(f'{contador2}° mês: R${montante:.2f}')
    contador2 += 1

print('3ex8 ^^^\n')

'''9. Crie um programa em linguagem Python que permite ao usuário inserir os valores dos
produtos comprados por um cliente. O programa deve terminar quando o usuário inserir o
valor 0. Se o usuário digitar um valor negativo não deve ser processado e um novo valor
deve ser solicitado como entrada. Ao final, informe o valor total a pagar, lembrando que,
caso as vendas ultrapassem o total de R$ 1.000,00, deverá ser aplicado um desconto de
10%.'''

valor_total = 0

while True:
    valor_item = float(input('informe o valor do produto escolhido: '))
    if valor_item > 0:
        valor_total += valor_item
    elif valor_item < 0:
        print('operação invalida, digite um valor positivo: ')
    else:
        break

if valor_total > 1000:
    valor_total -= 0.10 * valor_total

print(f'o valor total a ser pago é de: R${valor_total:.2f}.')

print('3ex9 ^^^\n')
print('FIM')