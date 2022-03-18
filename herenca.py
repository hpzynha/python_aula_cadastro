from datetime import date

class Pessoa:
    def __init__(self, **atributos) -> None:
        self.nome = atributos.get('nome')
        self.endereco = atributos.get('endereco')

class Juridica(Pessoa):
    def __init__(self, **atributos) -> None:
        super().__init__(**atributos)
        self.cnpj = atributos.get('cnpj')
        self.data_abertura = atributos.get('data_abertura')

class Fisica(Pessoa):
    def __init__(self, **atributos) -> None:
        super().__init__(**atributos)
        self.cpf = atributos.get('cpf')
        self.data_nascimento = atributos.get('data_nascimento')

fisica = Fisica(nome= 'Larissa', endereco ='rua xpto', cpf='002.760.792-56', data_nascimento=date(1990,3,8))

print(f'{fisica.nome} - {fisica.endereco} - {fisica.cpf} - {fisica.data_nascimento}')

juridica = Juridica(nome='emporio', endereco ='rua xpto', cnpj='00093452-001', data_abertura=date(2000,3,4))
print(f'{juridica.nome} - {juridica.endereco} - {juridica.cnpj} - {juridica.data_abertura}')