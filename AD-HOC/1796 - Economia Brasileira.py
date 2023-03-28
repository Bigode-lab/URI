n = int(input())
opnioes = [int(x) for x in input().split()]
a = opnioes.count(0)
if a > n/2:
    print('Y')
else:
    print('N')