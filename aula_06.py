numero = 1

while numero <= 10:
    if numero == 5:
        numero = numero + 1
        continue # não printa o numero 5
    print(numero)
    numero += 1 # numero = numero + 1
else:
    print('elias') # so é executado quando o laço termina

num = int(input('digite o numero da tabuada: '))
contador = 1
print(f'{num} X {contador} = {num * contador}')
while contador < 10:
    contador += 1
    print(f'{num} X {contador} = {num * contador}')

'''
operadores de atribuição
= / x = 1
+= / x = x + 1
-= / x = x - 1
*= / x = x * 1
/= / x = x / 1
%= / x = x % 1
'''

# ex 1
n1 = 0

while n1 < 100:
    n1 += 1
    print(n1)

# ex 2
import time

n2 = 10
print(n2)

while n2 > 1:
    time.sleep(1)
    n2 -= 1
    print(n2)
else:
    print('Fogo!')

# ex 3
primeiro_termo = int(input('informe o 1º termo da PA: '))
razao = int(input('informe a razão da PA: '))
contador = 1
termo_anterior = primeiro_termo
print(primeiro_termo)

while contador < 10:
    proximo_termo = termo_anterior + razao
    print(proximo_termo)
    termo_anterior = proximo_termo
    contador += 1