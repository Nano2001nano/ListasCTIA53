assentos = int(input("\nInforme o número de assentos: "))
valor_ingreco = float(input("Informe o valor do ingresso: "))
#entrada de dados

ingresso_final = round(0.90 * valor_ingreco, 1)
valor_ocupacao_total = round(ingresso_final * assentos,1)
setecinco_ocupacao = round(0.75 * (assentos * ingresso_final),1)
perda = round(assentos * (valor_ingreco * 0.10),1)
#processamento de dados

print(f"""\nValor do ingresso com desconto de 10%: R$ {ingresso_final}
            
            Valor que o teatro arrecadará com 100% de ocupação: R$ {valor_ocupacao_total}
            Valor que o teatro arrecadará com 75% de ocupação: R$ {setecinco_ocupacao}
            Valor que o teatro deixará de arrecadar com a promoção caso a ocupação seja de 100%: R$ {perda}\n""")
#saída de dados