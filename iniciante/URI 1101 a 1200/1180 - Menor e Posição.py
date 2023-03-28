m = int(input())
a = [int(x) for x in input().split()]
n = a[0]
p = 0
for x in range(m):
    if a[x] < n:
        n = a[x]
        p = int(x)
        
print('Menor valor: {}'.format(n))
print('Posicao: {}'.format(p))