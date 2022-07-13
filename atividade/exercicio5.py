numero = int(input("Digite um numero"))
operracao = input("Digite a operacao")

if operracao == "+":
    for x in range(1, 10):
        print(f"{x} + {numero} = {x + numero}")
elif operracao == "-":
     for x in range(1, 10):
        print(f"{x} - {numero} = {x - numero}")