'''
1. Elabore um programa que peça 3 números inteiros. Calcule e imprima
    a. o produto do triplo do segundo com metade do primeiro.
    b. A soma do dobro do terceiro com o segundo.
'''

num1 = float(input('1. digite um numero: '))
num2 = float(input('2. digite um numero: '))
num3 = float(input('3. digite um numero: '))

print(f'Letra A: {(num2*3)*(num1/2)}')
print(f'Letra B: {(num3*2)+(num2)}')