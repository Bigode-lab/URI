j = True
while j:
    a , b = (int(x) for x in input().split(' '))
    if a > b:
        print('Decrescente')
    elif a < b:
        print('Crescente')
    else:
        j = False