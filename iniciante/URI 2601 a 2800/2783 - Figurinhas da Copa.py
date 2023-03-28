n, c , m = (int(x) for x in input().split())
carimbadas = [int(x) for x in input().split()]
compradas = [int(x) for x in input().split()]
z = set()
for x in compradas:
    z.add(x)
for x in z:
    if x in carimbadas:
        c -= 1
print(c)