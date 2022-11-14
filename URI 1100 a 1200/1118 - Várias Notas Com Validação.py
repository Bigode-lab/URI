cont = 0
t = 0
j = True
while j:
    n = float(input())
    if n >= 0 and n <=10:
        cont += 1
        t += n
        if cont == 2:
            t = t/2
            print('media = {:.2f}'.format(t))
            z = True
            while z:
                a = int(input('novo calculo (1-sim 2-nao)\n'))
                if a == 2:
                    j = False
                    z = False
                elif a == 1:
                    cont = 0
                    t = 0
                    z = False
    else:
        print('nota invalida')