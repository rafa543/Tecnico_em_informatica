# frase = 'Centro de educação Profissional (SRB)'
# tamanho_frase = len(frase)
# contador = 0

# # while contador < 10:
# #     print(contador)
# #     contador += 1

# while contador < len(frase):
#     print(frase[contador], contador)
#     contador += 1


# frase = 'O rato roeu a roupa do rei roma'
# tamanho_frase = len(frase)
# contador = 0
# nova_string = ''

# while contador < tamanho_frase:
#     letra = frase[contador]
#     nova_string += letra
#     contador += 1

# print(nova_string.upper())
# print(nova_string.lower())
# print(nova_string.title())

# for i in nova_string:
#     if(i == "r"):
#         print(i.upper())
#     else:
#         print(i)

frase = 'O rato roeu a roupa do rei roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

# while contador < tamanho_frase:
#     letra = frase[contador]
#     nova_string += letra
#     contador += 1

letraInput = input("Qua letras vc quer que fique maiuscula?")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letraInput:
        nova_string += letraInput.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string) 

 

