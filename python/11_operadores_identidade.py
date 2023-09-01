curso = " curso de python"
nome_curso = curso 

print(curso is nome_curso) # comparo se os dois ocupam o mesmo espaço na memoria

curso is not nome_curso # os dois utilizam a mesma regiao de memoria e não curso retorna false 

saldo = 1000
limite = 200

print(saldo is limite) # pergunta saldo ocupa o mesmo espaço na memoria de limite retorna false 
print(saldo is not limite) # saldo não ocupa espaço na memoria de limite 
x=(22-10)*3
print(x)