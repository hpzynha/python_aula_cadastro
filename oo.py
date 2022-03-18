from datetime import date, datetime

class Funcionario:
    def __init__(self, **atributos):
        self.nome = atributos.get('nome')
        self.sexo = atributos.get('sexo')
        self.salario = atributos.get('salario')
        self.data_aniversario = atributos.get('data_aniversario')

    def calcular_idade(self):
        agora = datetime.now().date()
        diff = agora - self.data_aniversario
        return int(diff.days / 365)



f1 = Funcionario()
f1.nome = 'Larissa'
f1.sexo = 'F'
f1.salario = '3000'
f1.data_aniversario = date(1990, 3, 8)
print(f'{f1.nome} - {f1.data_aniversario}')
print(f1.calcular_idade())



f2 = Funcionario()
f2.nome = 'Stella'
f2.sexo = 'F'
f2.salario = '6000'
f2.data_aniversario = date(1991, 12, 28)
print(f'{f2.nome} - {f2.data_aniversario}')
print(f2.calcular_idade())

f3 = Funcionario()
f3.nome = 'Rodrigo'
f3.sexo = 'M'
f3.salario = '3000'
f3.data_aniversario = date(2002,11, 18)
print(f'{f3.nome} - {f3.data_aniversario}')
print(f3.calcular_idade())

