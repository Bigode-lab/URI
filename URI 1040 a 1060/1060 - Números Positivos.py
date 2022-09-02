positivo = 0
for x in range(6):
    n = int(input())
    if n >= 0:
        positivo += 1
print('{} valores positivos'.format(positivo))