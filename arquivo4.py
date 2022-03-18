with open('primeiro.text', 'r') as arquivo:

    linhas = arquivo.readlines()



    for linha in linhas:

        print(linha)



# arquivo.close()