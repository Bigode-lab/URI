j = True
while j:
    x , y = (int(z) for z in input().split(' '))
    if x > 0 and y > 0:
        print('primeiro')
    elif x > 0 and y < 0:
        print('quarto')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x == 0 or y == 0:
        j = False