'''
4. Construa um programa que gere e imprima a sequência de números ímpares de 1 até um
número inserido pelo usuário.
'''

num = int(input('digite um numero: '))

for i in range(1, num+1, 2):
    print(i)