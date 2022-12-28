import math
numero = int(input())
p = numero/math.log(numero)
m = 1.25506 *(numero/math.log(numero))
print('{:.1f} {:.1f}'.format(p, m))
