cont = 0
t = 0
while cont <= 2:
    n = float(input())
    if n >= 0 and n <=10:
        cont += 1
        t += n
        if cont == 2:
            t = t/2
            print('media = {:.2f}'.format(t))
    else:
        print('nota invalida')