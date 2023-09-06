# exemplo 1 if else 
"""
saldo = 2000.0
saque = float(input("digite o valor saque"))

if saldo >= saque:
    print("realizando saque")
else:
    print("saldo insuficiente")    

# exemplo 2 if elif else

opcao = int(input("informe a opção:[1] Sacar \n [2] Extrato : "))
if opcao == 1  :
    valor = float(input("informe a quantia do saque ; "))
elif opcao == 2 :
    print("exibindo o extrato")
else: 
    print("opção inválida")    
    
"""    
# if aninhado
"""
   
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500

cheque_especial = 450 

if conta_normal:
    if saldo >= saque :
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com o uso do cheque especial")
    else:
        print("NÃO FOI POSSIVEL REALIZAR O SAQUE")
elif conta_universitaria:
    if saldo >= saque:
         print("saque realizado com sucesso")
    else:
        print("saldo insuficiente")   

 """
 # if ternario

saque = 500
saldo = 600

#       1 condicao >>>>>>>>>>>>>>>>>>>>>> 2 condicao 
status = "sucesso " if saldo >= saque else "falha"
print(f'{status} ao realizar o saque')


