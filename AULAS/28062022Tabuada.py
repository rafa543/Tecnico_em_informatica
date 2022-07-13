num = int(input("Digite um numero: "))
operacao = input("Qual a operacao (+. -): ")


contador = 1
for i in range(1, 11):
    if operacao == "+":
        print(f'{contador} + {num} = {num + contador}')
        contador += 1
    else:
        print(f'{num} - {contador} = {num - contador}')
        contador += 1