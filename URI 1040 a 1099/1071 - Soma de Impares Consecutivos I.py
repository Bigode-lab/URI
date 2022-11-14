soma = 0
n1 = int(input())
n2 = int(input())
a = n2%2
if a == 0 and n1!= n2:
    n2 += 1
    while n2 < n1:
        soma += n2
        n2 += 2
elif a != 0 and n1!= n2:
    n2 += 2
    while n2 < n1:
        soma += n2
        n2 += 2
print(soma)