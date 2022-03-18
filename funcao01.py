def hello_world(nome):
    return f'Olá {nome}'


def hello_world2(nome:str) -> str:
    return f'Olá {nome}'

resultado = hello_world('Izzie')
print(resultado)

resultado = hello_world2('Osenias')
print(resultado)