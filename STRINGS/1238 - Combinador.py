teste = int(input())
for x in range(teste):
    aux = ''
    p1, p2 = (str(x) for x in input().split())
    a = max(len(p1), len(p2))
    if a == len(p1):
        for x in range(a):
            aux += p1[x]
            if x < len(p2):
                aux += p2[x]
    elif a == len(p2):
        for x in range(a):
            if x < len(p1):
                aux += p1[x]
            aux += p2[x]
    print(aux)
