# conjuntos dados set 

# criar conjuntos coleção de objetos unicos elimina os itens duplicados 

lista = set([1,2,3,4,5,3,4,])
print(lista)
# {1,2,3,4,5}

print(set("abacaxi"))
linguagens = {"java","javascript","c","java"}
print(linguagens)

# acessando os dados 
# conjuntos não permitem indexação e fatiamento 
# converter o set para uma lista 

conversao = list(linguagens)

print(conversao[0])


#iterar conjuntos 
carros = {"gol","uno","fusca"}
for carro in carros:
 print(carros)

# função enumerate
for indice , carro in enumerate(carros):
 print(f'{indice}:{carro}')

# métodos classe set
#Union dos conjuntos
conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))


# intersection meio dos conjuntos
c_a = {1,2,3}
c_b ={2,3,4}

print(c_a.intersection(c_b))

# difference

print(c_a.difference(c_b))
print(c_b.difference(c_a))

# simteric difference i que não tem no conjunto A e no B 

print(c_a.symmetric_difference(c_b))

# issubset não pertence e pertence 
conjunto_R = {1,2,3,} # pertence ao conjunto E true 
conjunto_E = {4,1,2,5,6,3} # falso não pertence 

print(conjunto_R.issubset(conjunto_E)) # true 
print(conjunto_E.issubset(conjunto_R)) # false


#issuperset é o contario 

#isdijont
conjunt_a = {1,2,3,4,5}
conjunt_b = {6,7,8,9}
conjunt_c = {1,0}

print(conjunt_a.isdisjoint(conjunt_b))
print(conjunt_a.isdisjoint(conjunt_c))

# adicionar um elemento no conjunto se existir ele nã adiciona 

sorteio = { 1, 23}
sorteio.add(25)
print(sorteio)

# limpar clear
sorteio.clear()
print(sorteio)



# copy 
sorteio = { 1, 23}
print(sorteio.copy())

# discard 
discarte = {1,2,3,4,5,67,89}
discarte.discard(1)
print(discarte)

# .pop tira os valores da lista
discarte.pop()
print(discarte)

# remove retorna erro se o elemento não existe 
discarte.remove(89)
print(discarte)

# len tamanho do conjunto 
print(len(discarte))


# In verificar se o objeto esta na minha lista

3 in discarte # True
1 in discarte # false


