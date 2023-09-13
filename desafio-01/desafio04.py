valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
for ano in range(periodo):
    #valor_final *= (1 + taxa_juros)
    valor_final = (valor_inicial * (taxa_juros + 1) ** periodo)

            
      

print(f"Valor final do investimento: R$ {valor_final:.2f}")
