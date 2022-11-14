j = True
a = 0
g = 0
d = 0
while j:
    n = int(input())
    if n == 1:
        a += 1
    elif n == 2:
        g += 1
    elif n == 3:
        d += 1
    elif n == 4:
        j = False
print('MUITO OBRIGADO')
print('Alcool: {}'.format(a))
print('Gasolina: {}'.format(g))
print('Diesel: {}'.format(d))