# 1 - Faça~um codigo que leia (funçao input()) leia um numero inteiro digitando pelo usuario
# e imprima (funçao print()) na tela do terminal se o numero e par ou impar 
# (use o operador % para avaliar.)

numero = int(input("Digite um numero para verificação "))
if (numero % 2) == 0:
    print(f'O numero {numero} e par')
else:
    print(f'O numero {numero} e Impar')