# numeros = range(100)
numeros = input('Digite os numeros separado por (,): ').split(',')
pares = 0
impares = 0

for n in numeros:
    if int(n) % 2 ==  0:
        pares += int(n)
    else:
        impares += int(n)

print(f'soma dos pares {pares}')
print(f'soma dos impares {impares}')