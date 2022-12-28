numero = int(input())
numero = str(numero)
for x in range(len(numero)):
    print(f'{numero[-(x+1)]}',end='')
print('\n')
