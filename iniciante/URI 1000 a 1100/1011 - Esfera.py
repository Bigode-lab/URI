#objetivo calcular o volume da esfera
import math
#importação da biblioteca math
raio = float(input())
#leitura de um valor de ponto flutuante e armazenando na variavel raio
volume = (4/3)*3.14159*(pow(raio, 3))
#calculando o volume da esfera
print('VOLUME = {:.3f}'.format(volume))