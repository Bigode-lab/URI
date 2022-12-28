n = int(input())
for x in range(n):
    a, b = (str(x) for x in input().split())
    if a == 'Thor':
        print('Y')
    else:
        print('N')
