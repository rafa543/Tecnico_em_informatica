arquivo = open("pessoas.txt", "a+")

while True:
    novoNome = input("Nome da pessoa:  ")
    arquivo.write(f"{novoNome}\n")
    sair = input("Novo cadastro? S[im] ou N[ão]:")
    if sair.lower() == 's':
        continue
    else:
        break

# arquivo.close()

print("\nPessoas ja cadastrada.")
print("- - - - - - - - - - -- - - -")
arquivo = open("pessoas.txt", "r")

for linha in arquivo:
    linha = linha.strip()
    print(linha)

arquivo.close()