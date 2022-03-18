frutas = [

    {'nome': 'maça', 'fruta_vermelha': True},

    {'nome': 'pessego', 'fruta_vermelha': False},

    {'nome': 'laranja', 'fruta_vermelha': False},

    {'nome': 'morango', 'fruta_vermelha': True},

    {'nome': 'cereja', 'fruta_vermelha': True},

]


print(frutas)


frutas_vermelhas = filter(lambda fruta: fruta['fruta_vermelha'], frutas)

nomes_frutas_vermelhas = map(lambda fruta: fruta['nome'], frutas_vermelhas)


for f in nomes_frutas_vermelhas:

    print(f)
