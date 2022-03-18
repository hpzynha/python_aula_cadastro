idade = int(input('Digite sua idade: '))

print(idade)
print(type(idade))

if idade >= 18:
    print('Maior de idade')
elif idade >= 12 and idade < 18:
    print('Adolescente')
else:
    print('Criança')
