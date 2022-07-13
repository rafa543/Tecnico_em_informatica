preco = int(input("Qual o preço da mercadoria :"))
# prestacoes = int(input("Quantas prestaçoes :"))

# for n in range(1):
#     valorParcela = preco/prestacoes
#     print(f"{prestacoes}x de R$ {valorParcela:.2f}")


for c in range(1, 21):
    prestacoes = preco /c
    
    if(c >= 5):
    #  print("prestacao",prestacoes * 0.02)
     print(f"{c}x R$ {prestacoes   + prestacoes * 0.02}")   
    else:
        print(f"{c}x R$ {prestacoes:.2f}")

lista = ['a', 'b', 'c']        

for n in lista:
    print(n)