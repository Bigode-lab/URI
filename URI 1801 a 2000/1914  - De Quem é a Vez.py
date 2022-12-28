n = int(input())
for x in range(n):
    s1, p, s2, i = (str(x) for x in input().split())
    a, b = (int(x) for x in input().split())
    r = (a+b)%2
    if r == 0:
        if p == 'PAR':
            print(s1)
        else:
            print(s2)
    elif r != 0:
        if p == 'IMPAR':
            print(s1)
        else:
            print(s2)