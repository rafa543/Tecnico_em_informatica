# ######################################################################
# Escreva um programa que leia um número "n" e um número "x" e escreva o
# valor de "x" elevado por "n". Valores para teste:
#
# n    x       resultado
# -2  -4      (3.061616997868383e-17-0.5j)
# 5   1000    3.9810717055349727
# -3  1000    0.10000000000000002
# 9   1       1.0
# 70  0       0.0
# ######################################################################

n = int(input('Informe um inteiro para o radical "n": '))
x = int(input('Informe um inteiro para o radicando "x": '))
resultado = x ** n
print('A raiz de {0} por {1} é: {2}'.format(n, x, resultado))