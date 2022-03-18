arquivo = open('primeiro.text', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

arquivo = open('primeiro.text', 'a')

arquivo.write('\n' + 'SEGUNDA LINHA DO ARQUIVO')

arquivo.close()