dois = 0
cinco = 0
tres = 0
quatro = 0
n = int(input())
numeros = [int(x) for x in input().split()]
for x in numeros:
    if x%2 == 0:
        dois += 1
    if x%3 == 0:
        tres += 1
    if x%4 == 0:
        quatro += 1
    if x%5 == 0:
        cinco += 1
print(f'{dois} Multiplo(s) de 2\n{tres} Multiplo(s) de 3\n{quatro} Multiplo(s) de 4\n{cinco} Multiplo(s) de 5')