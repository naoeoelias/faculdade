'''
3. Faça um programa que verifique se um número inserido pelo usuário é múltiplo de 3 e/ou
de 5 e exiba mensagens correspondentes, como "Múltiplo de 3", "Múltiplo de 5" ou
"Múltiplo de 3 e 5".
'''

num = int(input('digite um numero: '))


if num % 3 == 0 and num % 5 == 0:
    print('esse numero é multiplo de 3 e 5')
elif num % 3 == 0:
    print('esse numero é multiplo de 3')
elif num % 5 == 0:
    print('esse numero é multiplo de 5')
else:
    print('esse numero não é multiplo de nenhum dos dois')