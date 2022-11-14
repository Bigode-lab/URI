n = int(input())
for x in range (n):
    a = [float(x) for x in input().split(' ')]
    t = (a[0] * 2) + (a[1]*3) + (a[2]*5)
    r = t/10
    print(f'{r:.1f}')