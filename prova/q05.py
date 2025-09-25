'''
5. Escreva um programa que solicite ao usuário que insira uma sequência de números até que
ele insira um número repetido. O programa deve identificar o primeiro número repetido e
informá-lo.
'''

numeros = []

while True:
    num = int(input('digite um numero: '))
    if num in numeros:
        print(f"numero repetido: {num}")
        break
    numeros += [num]