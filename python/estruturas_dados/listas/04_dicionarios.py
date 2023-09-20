# dicionarios é um conjunto não ordenado chave e valor 

pessoa = {"nome":"Guilherme","idade":25}

p = dict(nome = "Guilherme", idade = 42)

pessoa["telefone"]="3333-1224" # adicionando uma nova chave 



# adicionando valores a dicionario 

pessoa["email"] = "cromulo.romulo@gmail.com"

#print(pessoa)

# dicionarios aninhados 
# objeto imutavel 
contatos = {
    "guilermepenteado@gmail.com":{"nome":"guilherme","telefone":"33333-3333"},
    "raul23@gmail.com":{"nome":"raul","telefone":"2222-3333"},
    "giovanaconelli@gmail.com":{"nome":"geovana conelli","telefone":"2345-5551"}
}
#print(contatos["giovanaconelli@gmail.com"]["telefone"])


# iterar for
for chave in contatos:
    print(chave, contatos[chave])

for chave,valor in contatos.items():
    print(chave, valor)    


# métodos da classe list

# .clear()
contatos.clear()
print(contatos) #{}


#.copy()
copia = contatos.copy()
print(copia)


dicionario = {

}
# .fromkeys cria chaves 
dicionario.fromkeys(["nome","telefone"]) # cria a chaves vazia 

dicionario.fromkeys(["nome","telefone"],"valor") # coloca valor nas chaves 

print(dicionario)



# .get verificar a chave se existe no dicionario
cont = {
    "raul@gmail.com":{"nome":"raul","telefone":"2423-1221"}
}

#cont["chave"] key error

#cont.get("chave") # none
cont.get("chave",{}) # {}
print(cont.get("raul@gmail.com",{}))


#.items() 
contatos_1 = {
    "raul@gmail.com":{"nome":"raul","telefone":"2423-1221"}
}
print(contatos_1.items()) # dict_items

#.keys retorna só as chaves 
contatos_1.keys() # dict_keys (["raul@gmail.com"])

# .pop remove a chave do seu dicionario 
print(contatos_1.pop("raul@gmail.com"))
# e também se ela não existir podemos colocar um valor padrão para ela retornar 

print(contatos_1.pop("raul@gmail.com",{})) # {}


# .popitem() retira os itens na sequencia e se ele não encontar mais nada no dicionario ele retorna um key error 
#contatos_1.popitem()
#contatos_1.popitem()# key error



# .setdefault se estiver no dicionario ele não altera ele 

carros = {"carro":"uno","ano":1980}
carros.setdefault("dono","mateus")
print(carros)

# .update() atualiza o nosso dicionario com o novo valor 

carros.update({"carro":"ferrai"})
print(carros)

# .values só retorna os valores sem as chaves
print(carros.values())


# in 
#"carro" in carros # true retorna true verifica se esxiste a chave carro no meu array
#"carro" in carros["celta"] # false não tem celta em carro



# .del remover deleta apenas a chave ou toda a linha que eu quero com chave e valor  
casas = {
"casa": {" nome":"rodolfo","telefone":"2213-4123"},

 
}

del casas["casa"]["telefone"] # ou apenas a chave telefone
del casas["casa"] # tudo que eu quero 
print(casas)

