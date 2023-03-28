import math
n = int(input())
parcela = (1 + math.sqrt(5))/2
parcela2 = (1 - math.sqrt(5))/2
fibo = (pow(parcela, n) - pow(parcela2, n))/math.sqrt(5)
print('{:.1f}'.format(fibo))