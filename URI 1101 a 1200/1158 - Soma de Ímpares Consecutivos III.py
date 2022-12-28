soma = 0
cont = 0
n = int(input())
for x in range (n):
    a, b  = (int(y) for y in input().split())
    while cont < b:
        t = a%2
        if t != 0:
            soma += a
            cont += 1
        a += 1
    print(soma)
    soma = 0
    cont = 0