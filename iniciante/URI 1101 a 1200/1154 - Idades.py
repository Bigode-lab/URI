cont = 0
soma = 0

j = True
while j:
    n = int(input())
    if n >= 0:
        soma += n
        cont += 1
    else:
        j = False
r = soma/cont
print('{:.2f}'.format(r))