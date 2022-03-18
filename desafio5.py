funcionarios = []


def exibir_menu():
    print('1 - Adicionar funcionário')
    print('2 - Soma do salário dos homens')
    print('3 - Soma do salário das mulheres')
    print('4 - Listar todos')
    print('0 - Sair do programa')
    print('-' * 20)


def cadastrar_funcionario():
    funcionario = dict()
    funcionario['nome'] = input('Digite o nome: ')
    funcionario['sexo'] = input(
        'Digite o sexo (M - Masculino, F - Feminino): ')
    funcionario['salario'] = float(input('Digite o salário: '))
    return funcionario


def totalizar(sexo='F'):
    filtrado = filter(
        lambda funcionario: funcionario['sexo'] == sexo, funcionarios)
    total = sum(map(lambda funcionario: funcionario['salario'], filtrado))
    return total


def main():
    while True:
        exibir_menu()
        opcao = int(input('Escolha sua opção: '))
        if opcao == 0:
            break
        elif opcao == 1:
            funcionarios.append(cadastrar_funcionario())
        elif opcao == 2:
            total = totalizar(sexo='M')
            print(f'Soma do salário dos homens {total}')
        elif opcao == 3:
            total = totalizar()
            print(f'Soma do salário dos mulheres {total}')
        elif opcao == 4:
            print(
                ', '.join(map(lambda funcionario: funcionario['nome'], funcionarios)))
        else:
            print('Opção inválida')


main()
