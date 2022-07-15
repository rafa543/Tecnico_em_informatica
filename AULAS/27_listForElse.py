var_lista = ["Ruby", "Java", "C++", "Python", "C#", "Javascrit", "C"]

for valor in var_lista:
    print(valor)
    continue
else:
    print("Fim do laço for")

for valor in var_lista:
    print(valor, end=" ")
    if valor.lower().startswith("c"):
        print("Inicia com C")
    else: 
        print("Nao inicia com C")

string_a = "Python é fenomenal, Python é para proposito geral"

lista_a = string_a.split(" ")
print(f"Lista_a: {lista_a}")

lista_b = string_a.split(", ")
print(f"Lista_b: {lista_b}")

for valor in lista_a: 
    print(f"A palavra {valor} apareceu {lista_a.count(valor)} x na frase ")

palavra = ""
contagem = 0

for valor in lista_a:
    qtd_vezes = lista_a.count(valor)
    if qtd_vezes > contagem :
        contagem = qtd_vezes
        palavra = valor

print(f"Palavra campea da lista_a: {palavra} x {contagem}")