medidas = int(input())
alturas = [int(x) for x in input().split()]
if medidas == 2 and alturas[0] == alturas[1]:
    r = 0
else:
    r = 1
    for i in range(1, medidas-1):
        if not ((alturas[i] < alturas[i-1] and alturas[i] < alturas[i+1]) or (alturas[i] > alturas[i-1] and alturas[i] > alturas[i+1])):
            r = 0
            break

print(r)
