'''
Exercicio 1º
Escreva um programa com base nos recursos
mostrados acima, mas que escreva no terminal as informaçoes no seguinte layout
'''

for x in range(0, 11):
    print(x, end= ' ')
print()

for y in ('Python'):
    print(y, end='')
print()

for y in ('Python'):
    print(y)
print()


print("CPF: 824", "176", "070", sep=".", end="-")
print("18")

txt = "For only {price:.3f} dollars!"
print(txt.format(price = 49))
