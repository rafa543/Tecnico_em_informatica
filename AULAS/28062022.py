

while True:
    print("Para encerrar digite s")
    nome = input("Qual o seu nome?")
    if nome.lower() == 's':
        break
    else:
        idade = int(input("Qual sua idade?"))

        if(idade >= 18):
            print("{0} você pode entrar".format(nome))
        else:
            print("{0} você e menor de idade".format(nome))


print("Programa encerrado com sucesso")    
