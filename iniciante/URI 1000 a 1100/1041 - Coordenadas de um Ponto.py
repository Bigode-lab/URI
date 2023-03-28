#objetivo dada uma cordenda julgar aodne ela se encontra
x, y = (float(x) for x  in input().split())
#leitura de uma cordenada
if (x>0 and y>0):
    print("Q1")
elif (x<0 and y>0):
    print("Q2")
elif (x<0 and y<0):
    print("Q3")
elif (x>0 and y<0):
    print("Q4")
elif (x == 0 and y == 0):
    print("Origem")
elif (x == 0 and y != 0):
    print("Eixo Y")
elif (x != 0 and y == 0):
    print("Eixo X")
#analise e impressao de qual quadrante a cordenada e ou se esta nos eixos ou na origem