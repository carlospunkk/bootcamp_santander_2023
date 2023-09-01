saldo = 1000
saque = 200
limite = 100

saldo >= saque # true
saque <= limite # false

# operador E ou AND quando os dois forem verdadeiros retorna true se não é false

saldo >= saque and saque <= limite # retorna false

# operador Or ou Ou . ou um ou outro é verdadeiro retorna verdadeiro
saldo >= saque or saque <= limite

# operador de negação
contatos_emergencia = []

not 1000 > 1500 #retorna o contrario com not 
not contatos_emergencia # retorna true 
not "saque 1500"  #retorna false

not "" # false

print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)