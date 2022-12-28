n = int(input())
for x in range(n):
    r1 , r2 = (int(x) for x in input().split())
    print(f'{r1 + r2}')