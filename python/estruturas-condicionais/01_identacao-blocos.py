
valores = input("digite um valor para sacar")

def sacar(valor):
    saldo = 50 
    if saldo >= valor:
        saldo = saldo - valor
        print(f'saque de :{valor}')
        print(f'saldo de : {saldo}')
    print("obrigado por ser nosso cliente")    

def depositar(valor):
    saldo = 500 
    saldo += valor  
    print(f'voce depositou {valor} e o total é : {saldo}')       

sacar(int(valores))        
depositar(30)




