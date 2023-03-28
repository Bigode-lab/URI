#dado 3 valores calcular a area de 5 figuras
import math
#importação da biblioteca math
a, b, c = (float(x) for x in input().split())
#leitura de 3 valores de ponto flutuante
triangulo = (a*c)/2
#calculo da area do triangulo
circulo = pow(c, 2)*3.14159
#calculo da area do circulo
trapezio = ((a + b)*c)/2
#calculo da area do trapezio
quadrado = pow(b, 2)
#calculo da area do quadrado
retangulo = a*b
#calculo da area do retangulo
print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
#impressao das areas