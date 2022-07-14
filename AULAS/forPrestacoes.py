preco = int(input("Qual o preço da mercadoria :"))

for c in range(1, 21):
    prestacoes = preco /c
    
    if(c >= 5):
        prestacaoComJuros = prestacoes   + prestacoes * 0.02
        print(f"{c}x R$ {prestacaoComJuros:.2f}")   
    else:
        print(f"{c}x R$ {prestacoes:.2f}")

