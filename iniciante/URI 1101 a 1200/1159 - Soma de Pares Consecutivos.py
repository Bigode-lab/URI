j = True
cont = 0
soma = 0
while j:
    a = int(input())
    if a != 0:
        while cont < 5:
            t = a%2
            if t == 0:
                soma += a
                cont += 1
            a += 1
        print(soma)
        soma = 0
        cont = 0
    else:
        j = False