campo = 'meu campo'



funcionario = dict()



funcionario['nome'] = 'Osenias Oliveira'

funcionario['idade'] = 34

funcionario['sexo'] = 'Masculino'



print(funcionario)



funcionario['salario'] = 1000.0

funcionario[campo] = 'CAMPO CUSTOMIZADO'



print(funcionario['meu campo'])



print(funcionario)



print(funcionario['nome'])

print(funcionario.get('nome'))



print(funcionario.get('salario', 0))




print(funcionario.keys())

print(funcionario.values())

print(funcionario.items())