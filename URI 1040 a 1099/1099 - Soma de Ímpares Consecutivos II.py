r = 0
n  = int(input())
for x in range(n):
    a , b = (int(x) for x in input().split(' '))
    r = 0
    if a == b:
        r = 0
        print(r)
    elif a > b:
        while b < a:
            b += 1
            j = b%2
            if j != 0 and a!=b:
                r += b
        print(r)
    elif b > a:
        while b > a:
            a += 1
            j = a%2
            if j != 0 and a != b:
                r += a
        print(r)