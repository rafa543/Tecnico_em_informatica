import sys

# arquivo = open('pessoas.txt', 'r')

# nomes = []

# for linha in arquivo:
#     nomes.append(linha.replace("\n", ""))
#     linha = linha.strip()
#     print(linha)

# arquivo.close()


# print(nomes)

arquivo = open('pessoas.txt', 'a+')


arquivo.write('Raimundo\n')
arquivo.write('Juliana\n')
arquivo.write('Rafael\n')

