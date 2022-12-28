soma = 0
j = True
while j:
    a, b = (int(x) for x in input().split())
    n = min(a, b)
    m = max(a, b)
    if n > 0 and m > 0:
        while n <= m:
            print("{}".format(n), end= ' ')
            soma += n
            n += 1
        print('Sum={}'.format(soma))
        soma = 0
    else:
        j = False