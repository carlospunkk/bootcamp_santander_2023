
frutas = ["laranja","morango","uva"]

frutas = []

letras = list('python')

numeros = list(range(10))

carro = ["ferrari",2000,True,'são paulo']



# acessando dados pelo indice 
frutas[-1] # uva
frutas[-2] # morango

#lista aninhada linhya e coluna lista dentro de lista

matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"]
],

matriz[0]#[1,"a",2] primeira linha
matriz[0][0] # 1 primeira linha primeiro item
matriz[0][-1] # 2 primeira linha ultimo item
matriz[-1][-1] # "c" ultima linha ultimo item 

# fatiamento acessar valor inicial ou valor final 

lista = ["p","y","t","h","o","n"]
lista[2:] # inicia do segundo elemento # ["t","h","o","n"]
lista[:2] # pega os dois primeiros     #["p","y"]
lista[1:3]# ["y","t"]
lista[0:3:2] #["p","t"] dois em dois
lista[:] # ["p","y","t","h","o","n"]
lista[::-1] # ["n","o","h","t","y","p"] inverte a ordem 



#iterar listas for
carros = ["gol","fiat","gurgel"]
for carro in carros:
    print(carro)

# função enumerate para saber qual o indice do objeto dentro do laço for 

for indice , carro in enumerate(carros):
    print(f"{indice}: {carro}")


# compresão de lista sintaxe mais curta quando vc deseja criar uma nova lista com base nos valores de uma lista existente

#versao 1
numeros = [1,30,22,43,24,25,50,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# versao 2 
#numeros = [1,30,22,43,24,25,50,34]
#pares = [numero for numero in numeros if numero % 2 == 0]

# numeros = [1,30,22,43,24,25,50,34]
# quadrado = [numero ** 2 for numero in numeros] # transforma tudo em quadrados 



# métodos adicionar elementos dentro da lista (append)
lista = [] 
lista.append(1)
lista.append("python")

lista.append([40,30,45])

# limpar lista (clear)
lista = [1,"python",[40,30,45]]
lista.clear()
# lista []

# copiar itens da lista (copy)
lista = [1,"python",[40,30,45]]
lista.copy()

# (count) conta quantos objetos com o mesmo nome tem na sua lista 
cores = ["verde","verde","azul"]
cores.count('vermelho') # 2
cores.count('azul') # 1

# juntar listas (extend)
linguagens = ["python",'js', 'c']
linguagens.extend(["java",'javascript']) # adicionar itens desta outra lista 

# (index) traz a primeira ocorrencia do item 
linguagens = ["python",'js', 'c','python']
linguagens.index('python') # 0 

# (pop) conceito de pilha o ultimo item colocado é o primeiro a ser tirado 
linguagens = ["python",'js', 'c','javascript']
linguagens.pop() # javascript
linguagens.pop() # "c"
linguagens.pop() # "js"
linguagens.pop(0) # "python" # indice que  quero remover 

# (remove) remover 
linguagens.remove('python') # remove o objeto elemento

# reverse
linguagens.reverse() # reverter lista

# (sort) ordena os elementos 
linguagens.sort() # ["c","js","javascript","python"]

# passando argumentos verfificando se o inverso é verdadeiro 
linguagens.sort(reverse=True) # ["python",'js', 'c','javascript']


# ordenar por tamanho da string palavra lambda função anonima (len) significa tamanho da string (x) SIGNIFICA A POSIÇÃO DE CADA ITEM DA LISTA 
linguagens.sort(key=lambda x:len(x)) # "javascript","python","js","c" 

# ordenar o inverso por tamanho 
linguagens.sort(key=lambda x:len(x), reverse=True) # "c", "js","python","javascript"

# (len) tamanho da lista 
materias = ["matematica","fisica","portugues"]
len(materias) # 5
    
    

# (sorted) função 
materias = ["matematica","fisica","portugues"] # ordena també por tamnanho de strings 
print(sorted(materias,key=lambda x: len(x)))# fisica portugues matematica 

#reverse
print(sorted(materias,key=lambda x: len(x),reverse=True)) # matematica portugues fisica