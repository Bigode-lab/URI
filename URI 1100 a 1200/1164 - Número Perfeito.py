n = int(input())
for y in range(n):
    z = int(input())
    soma = 0
    cont = 0
    x = 1
    while x < z :
        a = z%(x)
        if a == 0:
            soma += (x)
            cont += 1
        x += 1
    #soma -= n
    if soma == z:
        print('{} eh perfeito'.format(z))
    else:
        print('{} nao eh perfeito'.format(z))