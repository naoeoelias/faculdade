# exemplo senha 8 caracteres.

senha = input('digite uma senha de oito caracteres: ')

while len(senha) < 8:
    senha = input('a senha não possui 8 caracteres, digite outra senha: ')
else:
    print('operação concluida')

# peça ao usuario para inserir numeros inteiros ate que ele insira um numero negativo.
# calcule e imprima a soma apenas dos numeros pares inseridos.

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

# progressão aritmetica

primeiro_termo = int(input('informe o 1° termo da pa: '))
razao = int(input('informe a razão da pa: '))
numero_termos = int(input('informe o numero de termos da pa: '))
contador = 1 
termo_anterior = primeiro_termo
print(f'o {contador}° termo da pa é: {primeiro_termo}.')

while contador < numero_termos:
    proximo_termo = termo_anterior + razao
    termo_anterior = proximo_termo
    contador += 1
    print(f'o {contador}° termo da pa é: {proximo_termo}.')

# advinhar numero
import random

numero_sorteado = random.randint(1,10)
numero_escolhido = int(input('digite um numero inteiro: '))
tentativas = 1


while numero_escolhido != numero_sorteado:
    numero_escolhido = int(input('digite outro numero inteiro: '))
    tentativas += 1

print(f'parabens, {numero_sorteado} foi o numero sorteado. você acertou com {tentativas} tentativas.')