# q08

deposito_inicial = float(input('digite o valor inicial que sera depositado na poupança: '))
taxa_juros = float(input('digite a taxa de juros da aplicação: ')) / 100
contador = 1

while contador <= 24:
    montante = deposito_inicial * (1 + taxa_juros)** contador
    print(f'{contador}° mês: R${montante:.2f}')
    contador += 1

# q09

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

# for soletrar

nome = 'elias'

for cuscuz in nome:
    print(cuscuz)

# for contar vogais

palavra = input('digite uma palavra: ')
contador_vogal = 0

for cont in palavra:
    if cont in 'aeiou':
        contador_vogal += 1

print(f'a palavra {palavra} possui {contador_vogal} vogais.')