'''
2. Em um supermercado é oferecido um cupom de desconto que varia conforme o valor total
da compra. Informe o valor do desconto e o valor total a ser pago.
    • Para compras acima de R$500 e de até R$800, o cupom de desconto é de 7%.
    • Para compras entre R$800 e R$1000, o cupom é de 9%.
    • Para compras a partir de R$1000, o cupom é de 11%
'''

valor_compra = float(input('informe o valor da compra: '))
desconto = 0

if (valor_compra > 500) and (valor_compra < 800):
    desconto = 7 / 100
elif (valor_compra > 800) and (valor_compra < 1000):
    desconto = 9 / 100
elif valor_compra > 1000:
    desconto = 11 / 100

print(f'Valor do desconto: {(valor_compra * desconto):.2f}')
print(f'valor total a ser pago: {valor_compra - (valor_compra * desconto)}')