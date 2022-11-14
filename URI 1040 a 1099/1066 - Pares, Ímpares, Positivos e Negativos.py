pares = 0
impares = 0
positivos = 0
negativos = 0
for x in range(5):
    n = int(input())
    a = n%2
    if a == 0:
        pares += 1
    elif a != 0:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print('{} valor(es) par (es)'.format(pares))
print('{} valor(es) impar (es)'.format(impares))
print('{} valores positivo (s)'.format(positivos))
print('{} valores negativo s)'.format(negativos))