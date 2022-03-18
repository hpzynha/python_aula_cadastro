def somar(*numeros):
    acumulador = 0
    for n in numeros:
        acumulador += n
    return acumulador


resultado = somar(10, 20, 30)

print(resultado)

numeros = [10,20,30]
resultado = somar(*numeros)
print(resultado)