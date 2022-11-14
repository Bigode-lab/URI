pares = 0
for x in range(5):
    n = float((input()))
    a = n%2
    if a == 0:
        pares += 1
print('{} valores pares'.format(pares))