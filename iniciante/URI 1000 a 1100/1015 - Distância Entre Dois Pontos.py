#objetivo calcular a distancia entre dois pontos
import math
#importação da biblioteca math
x1, y1 = (float(x) for x in input().split())
x2, y2 = (float(y) for y in input().split())
#leitura dos pontos
distancia = math.sqrt(((pow((x2 - x1), 2))+((pow((y2 - y1), 2)))))
#calcular da distancia entre dois pontos
print('{:.4f}'.format(distancia))
#impressao da distancia
