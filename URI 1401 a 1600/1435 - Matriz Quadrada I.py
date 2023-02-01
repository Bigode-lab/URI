dln = 0
dl0 = 0
dcn = 0
dc0 = 0
l = []
c = []
n = int(input())
while (n != 0):
    if n == 1:
        print(f'{1}')
    else:
        for x in range(n):
            for y in range(n):
                dln = abs(n-x)
                dl0 = abs(x+1)
                dcn = abs(n-y)
                dc0 = abs(y+1)
                a = min(min(dln, dl0), min(dc0, dcn))
                if y < (n-1):
                    print(a, end='   ')
                elif y == (n-1):
                    print(a, end='\n')
                    print(end=' ')
                l.append(a)
            c.append(l)
            l = []
    #for a in c:
     #   print(*a)
    c = []
    print('')
    n =int(input())