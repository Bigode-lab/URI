n = int(input())
p = [int (x) for x in input().split()]
a = min(p)
print(p.index(a) + 1)