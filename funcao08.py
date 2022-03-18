frutas = ['maça', 'laranja', 'uva', 'manga']

def funcao_filtro(fruta):
    return fruta in ['maca', 'uva']

novas_frutas = filter(funcao_filtro, frutas)

for f in novas_frutas:
    print(f)
