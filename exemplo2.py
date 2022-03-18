def somar(a, b):
    if a > 10:
        raise Exception('O valor de A não pode ser maior que 10.')
    return a + b

while True:
    try:
        a = int(input('valor de a: '))
        b = int(input('valor de b: '))
        resultado = somar(a, b)
        print(resultado)
        break
    except Exception as error:
        print(error)
        # enviar um email
        # salvar o erro no arquivo
        continue