# Rafael Araujo 

import random

arquivo = open('alunos.txt', 'r')
nomes = []

for linha in arquivo:
    nomes.append(linha.replace("\n", ""))
    linha = linha.strip()
arquivo.close()

while len(nomes) != 0:
    random.shuffle(nomes)
    print(nomes[:4])
    nomes = nomes[4:]
