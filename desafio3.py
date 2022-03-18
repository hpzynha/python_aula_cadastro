palavra = input('Digite sua palavra: ')

total_vogais = 0

total_consoantes = 0

VOGAIS = ('a', 'e', 'i', 'o', 'u')



for letra in palavra:

    if letra.lower() in VOGAIS:

        total_vogais += 1

    else:

        total_consoantes += 1




print(f'Quantidade de vogais {total_vogais}')

print(f'Quantidade de consoantes {total_consoantes}')