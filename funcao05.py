from typing import List

def teste(*parametros):
    for p in parametros:
        print(f'dicionário: {p}')
        for key, value in p.items():
            print(f'key: {key} - value: {value}')


p1 = {'a': 10, 'b': 20}
p2 = {'a': 90, 'b': 102}
p3 = {'a': 100, 'b': 800}

teste(p1, p2, p3)


def teste2(items: List[int]):
    pass
