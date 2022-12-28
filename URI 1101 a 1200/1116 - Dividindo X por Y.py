n = int(input())
for x in range(n):
    a, b = (int(z) for z in input().split(' '))
    if b == 0:
        print('divisao impossivel')
    else:
        r = a/b
        print('{:.1f}'.format(r))