"""
Considere que as variáveis "dia", "mês" e "ano" contém os valores
respectivos de uma certa data. Escreva um comando "print" usando a
mensagem "format" que imprima essa data no formato usual, por
exemplo, "12/11/2016" ou "3/7/2011".
"""
dia = int(input("Escolha um dia? "))
mes = int(input("Escolha um mes? "))
ano = int(input("Escolha um ano? "))

print("{0}/{1}/{2}".format(dia, mes, ano))