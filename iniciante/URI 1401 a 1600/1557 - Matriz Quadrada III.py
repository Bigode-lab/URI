n =  int(input())
print(n)
matriz = []
linha = []
for i in range(n):
    for j in range(n):
        a = pow(2, (i+j))
        linha.append(a)
    matriz.append(linha)
    linha = []
for i in matriz:
    print(*i)
