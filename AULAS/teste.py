from ast import Break


texto = "Python V3"
url = "www.pi.senac.br/"

print(texto[:-3])
print(url[:-4])
print(len(url))

nova_string = texto[2:4]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[0:6:2]
print(nova_string)

nova_string = texto[0::3]
print(nova_string)

for letra in texto:
    print(letra, end='')

while True:
    nome = input("Qual e o seu nome?: ")
    print(f'Ola {nome}')

    parada = input("Deseja sair? :")
    if(parada == "s"):
        break

x = 0

while x < 5:
    print(f'Laço atual: {x}')
    x += 1
print("Laço encerrado!")

x = 0

while x < 10:
    if x == 6:
        x += 1
        continue
    print(f'laço atual: {x}')
    x+=1
print('Laço encerrado!')

x = 0

while x < 10:
    y = 0
    while y < 5:
        y += 1
        z = 0
        while z < 5:
            print(f'({x}, {y}, {z})')
            z += 1
    x += 1

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1


while True: 
    num_1 = input("Digite um numero: ")
    num_2 = input("Digite outro numero: ")
    operador = input("Digite um operador (+. -, /, **, // ou % ): ")