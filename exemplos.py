nome: str = 'Larissa'
sobre_nome = 'Rocha'
idade: int = 10
salario: float = 1000.00
casado = True

resultado = nome == 'larissa' and idade == 10

print(resultado)

resultado = nome == 'Rodrigo' or idade == 10

print(resultado)

resultado = 'O' in nome
print(resultado)


print(nome + ' - ' + sobre_nome)
print(f'{nome} - {sobre_nome}')
print('{} - {}'.format(nome, sobre_nome))


print(nome)
print(type(nome))
print(idade)
print(type(idade))

idade = 'oi'

print(idade)
print(type(idade))

print(salario)
print(type(salario))

print(casado)
print(type(casado))