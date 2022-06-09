totalSegundos = int(input("Informe o total de segundos "))
horas = totalSegundos // 3600
minutos = (totalSegundos % 3600) // 60
segundos = minutos // 60


segundos = totalSegundos % 60

print(horas, minutos, segundos)
print("{} horas {} minutos {} segundos".format(horas, minutos, segundos))
