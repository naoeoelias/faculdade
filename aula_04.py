idade = float(input('digite sua idade: '))
if idade >= 18:
    print('você é maior de idade e pode emitir a cnh')
else:
    print('você é menor de idade e não pode emitir a cnh')

# exemplo curso

curso = input('digite o curso que você vai fazer: ').lower()

if curso == 'medicina':
    print(f'o tempo de conclusão do curso {curso} é de 6 anos')
elif curso == 'ads':
    print(f'o tempo de conclusão do curso {curso} é de 2 anos')
elif curso == 'engenharia':
    print(f'o tempo de conclusão do curso {curso} é de 5 anos')
elif curso == 'nutrição':
    print(f'o tempo de conclusão do curso {curso} é de 4 anos')
else:
    print('o curso em questão não é ofertado.')

# pratica da aula
salario = float(input('Digite o valor do seu salario: '))
if salario > 1200:
    print('será necessario pagar imposto. :(')
else:
    print('não será necessario pagar imposto. :)')

# pratica 2 da aula
senha = input('digite sua senha: ').lower()
senha_armazenada = 'cuscuz'
if senha_armazenada == senha:
    print('Acesso permitido!')
else:
    print('Acesso negado!')

# pratica 3 da aula
salario = float(input('digite o valor do seu salario: '))
cargo = input('digite o nome do seu cargo: ')

if cargo == 'desenvolvedor':
    novo_salario = salario + 30/100 * salario
elif cargo == 'analista de sistemas':
    novo_salario = salario + 20/100 * salario
elif cargo == 'analista de banco de dados':
    novo_salario = salario + 15/100 * salario
else:
    print(f'para o cargo de {cargo} não foi previsto reajustes')

print(f'seu novo salario é de {int(novo_salario)}')

'''
operadores logicos
not
and
or
'''

# or
salario = float(input('digite o valor do seu salario: '))
cargo = input('digite o nome do seu cargo: ')

if cargo == 'desenvolvedor' or cargo == 'analista de sistemas':
    novo_salario = salario + 30/100 * salario
elif cargo == 'analista de banco de dados':
    novo_salario = salario + 15/100 * salario
else:
    print(f'para o cargo de {cargo} não foi previsto reajustes')

print(f'(or) seu novo salario é de {int(novo_salario)}')

# and
salario = float(input('digite o valor do seu salario: '))
cargo = input('digite o nome do seu cargo: ')
novo_salario = salario

if cargo == 'desenvolvedor' and salario < 7000:
    novo_salario = salario + 30/100 * salario
elif cargo == 'analista de sistemas':
    novo_salario = salario + 20/100 * salario
elif cargo == 'analista de banco de dados':
    novo_salario = salario + 15/100 * salario
else:
    print(f'para o cargo de {cargo} não foi previsto reajustes')

print(f'(and) seu novo salario é de {int(novo_salario)}')

# exemplo estudo dirigido
situacao = input('informe sua situação para usar a fila de prioridade (lactante, gestante, idoso, pcd): ')

if (situacao == 'lactante') or (situacao == 'gestante') or (situacao == 'idoso') or (situacao == 'pcd'):
    print('você tem direito de usar a fila de prioridade')
else:
    print('você não tem direito de usar a fila de prioridade')

# exemplo 2 estudo dirigido
num1 = int(input('digite o 1º numero inteiro: '))
num2 = int(input('digite o 2º numero inteiro: '))
num3 = int(input('digite o 3º numero inteiro: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} é maior que {num2} e {num3}')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é maior que {num1} e {num3}')
else:
    print(f'{num3} é maior que {num1} e {num2}')