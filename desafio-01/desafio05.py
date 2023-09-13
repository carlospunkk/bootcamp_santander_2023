valor = float(input())
#TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
if valor > 0:
    print(f"Deposito realizado com sucesso!\nSaldo atual: R$ {valor:.2f}")
elif valor == 0:
   #TODO: Imprimir a mensagem de valor inválido.
   print("Encerrando o programa...")
elif valor < 0:
  #TODO: Imprimir a mensagem de encerrar o programa.
  print("Valor invalido! Digite um valor maior que zero.")