a = [int(x) for x in input().split(' ')]
x = a[0]
y = a[len(a)-1]
cont = y-1
soma = 0
while cont < y and cont >= 0:
    soma += x+cont
    cont -= 1
print(soma)