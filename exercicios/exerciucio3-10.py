# ###############################################################################
# Escreva um programa que calcule em seguundos o tempo desde a última meia-noite.
#
# Valores para teste:
#
# Entradas                        Resultados
# Horas   Minutos     Segundos    Totais de segundos
# 5       12          0           18720
# 13      0           9           46809
# 21      45          59          78359
# 23      59          59          86399
###############################################################################
segundosTotal = 0

horas = input("Qual e a hora?")
segundosTotal += 3600 * int(horas)

minutos = input("Qual e o minutos?")
segundosTotal += 60 * int(minutos)

segundos = input("Qual e o minutos?")
segundosTotal += int(segundos)

print("Total em segundos", segundosTotal)