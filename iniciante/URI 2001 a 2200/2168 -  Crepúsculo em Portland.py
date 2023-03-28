n = int(input())
matriz = []
soma = 0
a = ''
for i in range(n+1):
        l = [int(x) for x in input().split()]
        matriz.append(l)

for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1:
            soma += 1
        if matriz[i][j+1] == 1:
            soma += 1
        if matriz[i+1][j] == 1:
            soma += 1
        if matriz[i+1][j+1] == 1:
            soma += 1
        if soma > 1:
            a += 'S'
            soma = 0
        else:
            a += 'U'
            soma = 0
    print(a)
    a = ''
