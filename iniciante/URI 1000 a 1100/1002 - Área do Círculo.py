#objetivo calcular a arear do circulo
import math
#importação da biblioteca math biblioteca de matematica
r = float(input())
#leitura de um valor de ponto flutuante
area = 3.14159*(pow(r,2))
#calculo da area
print('A={:.4f}'.format(area))
#impresao do valor da area com a limitacao de 4 casas decimais