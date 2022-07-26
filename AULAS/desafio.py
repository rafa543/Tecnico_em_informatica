import random
arquivo = open('alunos.txt', 'r')

nomes = []
grupo1 = []
grupo2 = []
grupo3 = []
grupo4 = []
grupo5 = []
grupo6 = []

grupos = []

for linha in arquivo:
    nomes.append(linha.replace("\n", ""))
    linha = linha.strip()
arquivo.close()

print(nomes.sort())

for index, nome in enumerate(nomes):
    print(index)
    if len(grupo1) < 4:
        grupo1.append(nome)
        continue

    if len(grupo2) < 4:
        grupo2.append(nome)
        continue

    if len(grupo3) < 4:
        grupo3.append(nome)
        continue

    if len(grupo4) < 4:
        grupo4.append(nome)
        continue
    
    if len(grupo5) < 4:
        grupo5.append(nome)
        continue

    if len(grupo6) < 4:
        grupo6.append(nome)
        continue

# print(nomes)

print(grupo1)
print(grupo2)
print(grupo3)
print(grupo4)
print(grupo5)
print(grupo6)

# print(random.choice(nomes))