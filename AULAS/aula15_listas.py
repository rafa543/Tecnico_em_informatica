# minah_lista = ["maria", "isadora", "Carmen", 1, 2, 3]

# print(minah_lista)

# for i in minah_lista:
#     print(i)

# lista = ['A', 'B', 'C', 'D', 'E', 1, 2, 3]

# print(len(lista))
# print(lista[3])
# print(lista[-8])
# print(lista[::-1])
# print(lista[3:])
# print(lista[:3])
# print(lista[::2])

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [7, 8, 9, 10, 11, 12]

print(f'lista1: {lista1}')
print(f'lista2: {lista2}')
print(f'Valor maximo lista1: {max(lista1)}')
print(f'Valor maximo lista2: {max(lista2)}')


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [7, 8, 9, 10, 11, 12]

print(f'Lista1: {lista1}')
print(f'Lista2: {lista2}')

lista1.append('a')
print('append:', lista1)

lista2.insert(0, "Chocolate")
print('insert: ', lista2)

lista1.pop()
print(lista1)

del(lista2[-1])

print("del: ", lista2)

lista2.remove("Chocolate")
print(lista2)

# lista2.clear()
# print(lista1)
