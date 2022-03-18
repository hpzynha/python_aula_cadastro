numeros = list(range(200))
menores_que_ou_igual_100 = []

# for n in numeros:
#     if n <= 100:
#         menores_que_ou_igual_100(n)

# mesma coisa da função filter()


menores_que_ou_igual_100 = [n for n in numeros if n <=100]

print(menores_que_ou_igual_100)