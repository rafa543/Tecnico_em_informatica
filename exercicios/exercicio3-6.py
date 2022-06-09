"""
Escreva um programa que leia um número inteiro "x"
e escreva o valor desse número elevado ao cubo x³.
Valores para teste:
Entradas    Resultado
x           x³
--          --
-5          -125
-1          -1
0           0
1           1
4           64
53          148877
"""

x = int(input('Informe um valor para x: '))

print('x recebeu {0}, esse valor ao cubo vale: {1}'.format(x, x * x * x))