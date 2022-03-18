funcionarios = []
homens = 0
mulheres = 0

while True:
    print('1 - Adicionar funcionarios')
    print('2 - Soma do salarios dos homens')
    print('3 - Soma do salário das mulheres')
    print('-' * 20)
    opcao = int(input('Escolha sua opção: '))

    if opcao == 0:
        break
    elif opcao == 1:
        funcionario = dict()
        funcionario['nome'] = input('Digite o nome: ')
        funcionario['sexo'] = input('Digite o Sexo: (M - Masculino, F - Feminino): ' )
        funcionario['salarios'] = float(input('Digite o salário: '))
        funcionarios.append(funcionario)
        if funcionario['sexo'] == 'M':
            homens +=funcionario['salarios']
        else:
            mulheres +=funcionario['salarios']
    elif opcao == 2: 
        print(f'soma dos salario dos homens {homens}')
    elif opcao == 3:
        print(f'soma dos salario dos mulheres {mulheres}')
    else:
        print('Opção inválida')
            