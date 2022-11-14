i = 0
j = 1
cont = 5
while i <= 2:
    if cont == 5:
        for x in range(3):
            print('I={:.0f} J={:.0f}'.format(i, j+x))
            cont = 0
    else:
        for x in range(3):
            print('I={:.1f} J={:.1f}'.format(i, j+x))
    i += 0.2
    j += 0.2
    cont += 1