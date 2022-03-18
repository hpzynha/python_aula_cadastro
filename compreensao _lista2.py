funcionarios = [
    {'nome' : 'Larissa', 'sexo': 'F', 'salario': 1000},
    {'nome' : 'Rodrigo', 'sexo': 'M', 'salario': 3000},
    {'nome' : 'Ruan', 'sexo': 'M', 'salario': 2000},
]

masculinos = sum([f['salario'] for f in funcionarios if f['sexo'] == 'M'])

print(masculinos)