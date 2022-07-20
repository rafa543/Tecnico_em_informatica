# string_a = "Python e fenomenal, python e para proposito geral."

# lista_b = string_a.split(" ")
# string_b = " ".join(lista_b)

# print(string_a)
# print(lista_b)
# print(string_b)

import random
string = "Python e fenomenal, python e para proposito geral."
lista = string.split(" ")

testeArray = []

for indice, valor in enumerate(lista):
    testeArray.append(valor)
    print(indice, valor)

print(testeArray[random.randint(0,len(testeArray) - 1)])

# import random

# x = random.randint(1,52)

# print(x)

# Criar uma lista com números entre 1 e 52
# cartas = list(range(1,53))

# print(cartas)

# random.shuffle(cartas)

# print(cartas)
