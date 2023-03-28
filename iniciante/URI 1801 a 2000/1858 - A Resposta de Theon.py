#imprimir a resposta onde a pessoa sofrera menos
n = int(input())
#leitura de um valor inteiro n 
p = [int (x) for x in input().split()]
#leitura dos valores representados por cada pessoa
a = min(p)
#a recebe o menor valor de p
print(p.index(a) + 1)
#impressao da possicao da pessoa