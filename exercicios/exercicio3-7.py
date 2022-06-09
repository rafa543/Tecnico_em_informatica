# #################################################
# Escreva um programa para calcular a raiz cubica
# de um número inteiro indicado pelo usuário.
#
# Valores para teste:
#
# x     Resultado
# -40	(1.7099759466766973+2.961765219364728j)
# -1	(0.5000000000000001+0.8660254037844386j)
# 0	    0.0
# 1	    1.0
# 64	3.9999999999999996
# 125	5.0
# #################################################

x = int(input('Informe um inteiro: '))
raizC = x ** (1/3)
print('A raiz cúbica de {0} é: {1}'.format(x, raizC))
