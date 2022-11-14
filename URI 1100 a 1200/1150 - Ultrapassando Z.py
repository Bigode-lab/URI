j = True
x = int(input())
while j:
    z = int(input())
    if z > x:
        j = False
a = []
a.append(x)
while sum(a) < z:
    x = x+1
    a.append(x)
print(len(a))