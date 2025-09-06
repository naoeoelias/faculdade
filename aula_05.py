
# exemplo 1
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

# exemplo 2
usuario = input('digite o seu usuario: ')
senha = input('digite a sua senha: ')

log_user = 'elias'
log_pass = 'cuscuz'

if (usuario == log_user) and (senha == log_pass):
    print(f'Bem Vindo {usuario}!')
else:
    print('Usuario e/ou senha não conferem.')

# exemplo 3
vel_veiculo = float(input('Digite a velocidade do veiculo: '))

if vel_veiculo > 80:
    valor_multa = (vel_veiculo - 80) * 5
    print(f'Você foi multado em R${valor_multa}.')
else:
    print('Você não foi multado')

# exemplo 4
distancia_percorrida = float(input('Digite a Distancia que será Percorrida: '))

if (distancia_percorrida >= 0) and (distancia_percorrida <= 200):
    valor_pago = 0.5 * distancia_percorrida
else:
    valor_pago = 0.45 * distancia_percorrida

print(f'o valor a ser pago vai ser de {valor_pago} reais.')

# exemplo 5
# escreva um programa que leia dois numeros e que pergunte qual operação você deseja realizar. você deve poder calcular soma subtração multiplicação e divisão exiba o resultado da operação solicitada
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