"""
Escreva um programa que leia três números inteiros nas variáveis
“a”, 'b” e “c” e escreva a média deles: (a+b+c)/3. Teste seu
programa pelo menos com pelo menos os valores indicados a seguir:
Valores para teste:
Entradas:
a   b   c   Resultado
3   5   13  7.0
20  15  3   12.666666666666666
0   0   0   0.0
"""
a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))

print('Valores informados: a -> {0} | b -> {1} | c -> {2}'.format(a, b, c))
print('Média de a + b + c = {0}'.format((a + b + c)/3))