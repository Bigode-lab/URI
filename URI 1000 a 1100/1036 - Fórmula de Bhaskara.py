#objetivo calcular 2 raizes de uma equacao do segundo grau utilizando bhaskara
import math
#importando a biblioteca math
a, b, c = (float(x) for x in input().split())
#leitura dos valores a, b, c 
delta = ((pow(b, 2)) - (4*a*c))
#calculo do delta
if (delta<0 or a == 0):
#vendo se é possivel calcular a rais 
    print("Impossivel calcular")
    #se nao for possivel calcular a raiz se imprime impossivel calcular
else:
    raiz  = math.sqrt(delta)
    r1 = (-b + raiz)/(2*a)
    print("R1 = {:.5f}".format(r1))
    r2 = (-b - raiz)/(2*a)
    print("R2 = {:.5f}".format(r2))

#se for possivel calcular se calcula r1 e r2 e as imprime