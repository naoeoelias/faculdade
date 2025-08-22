# imc = peso (altura**2)

peso = float(input('Insira seu Peso: '))
altura = float(input('Insira sua Altura: '))
imc = peso / (altura ** 2)
# no print pode concatenar com virgula ou + pelo oq entendi
print(f'Seu IMC é  {imc:.2f}')
# ou: print('seu IMC é ' + str(imc))
# ou ja converte na propria variavel

# desconto em um produto
preco = float(input('Insira o preço do produto: '))
percentual_desconto = int(input('Insira o valor do desconto do produto: ')) / 100

valor_desconto = preco * percentual_desconto
valor_final = preco - valor_desconto

print('o valor do desconto foi: ', valor_desconto, ' reais')
print(f'o valor do produto com desconto é: {valor_final} reais')

# velocidade media
distancia = int(input('Digite a distancia que será percorrida: '))
vmedia = int(input('Digite a velocidade media do veiculo: '))
tempo = distancia / vmedia
print(f'o tempo será de {tempo:.2f} horas')

# estudo dirigido
# 1ª questão
pnumero = int(input('digite o primeiro numero: '))
snumero = int(input('digite o segundo numero: '))
soma = pnumero + snumero
print(f' a soma dos dois numeros é de {soma}')

# 2ª questão
metros = float(input('digite um valor em metros: '))
milimetros = metros * 1000
print(f'o valor de {metros} em milimetros é de: {milimetros}')

# 3ª questão
porcentagem = 15 / 100
valor = 750
valor_aumento = valor * porcentagem
valor_final = valor + valor_aumento
print(f'o aumento de 15% no numero 750 é de: {valor_final}')

# 4ª questão
dolar = 4.96
valor = float(input('digite o valor a ser convertido: '))
conversao = valor * dolar
print(f'o valor({valor}) de dolares({dolar}) em reais é de: {conversao}')

# 5ª questão
celsius = float(input('digite o valor a ser convertido em ºF: '))
f = (9 * celsius / 5) + 32
print(f'o valor convertido de ºC para ºF é {f}')