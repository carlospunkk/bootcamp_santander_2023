dinheiro = 2.250

print(f"valor de dinheiro : {dinheiro:.2f}")

# formatando com espaços 10
print(f"valor de dinheiro : {dinheiro:10.2f}")


nome = 'carlos'
idade = 42

#format 
print("nome : {} idade : {} ".format(nome,idade))

# outra formatacao com array
dados = {"materia":"matematica","professor":"gustavo"}

print("materia : {materia} professor : {professor} ".format(**dados))