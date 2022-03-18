while True:
    try:
        numero =  int(input('Digite um número: '))
        print(numero)
    except ValueError:
        print('você só deve usar numeros')
        continue