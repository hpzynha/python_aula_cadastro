numeros = range(10)
for n in numeros:
    print(n)

def numero_par(numero):
    return numero %2 == 0

novos_numeros = filter(numero_par, numeros)
for n in novos_numeros: 
    print(n)