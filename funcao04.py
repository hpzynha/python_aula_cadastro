def calcular(**parametros):
    a = parametros.get('a')
    b = parametros.get('b')
    operador = parametros.get('operador')

    return eval(f'{a} {operador} {b}')


resultado = calcular(a=10, b=20, operador='+')

print(resultado)

parametros = {
    'a':10,
    'b': 20,
    'operador': '+'
}

resultado = calcular(**parametros)
print(resultado)
