#ler um valor e retornar o intervalo onde ele se encontra
n = float(input())
#leitura de um valor de ponto flutuante
if ((0<=n)and(n<=25)):
    print("Intervalo [0,25]")
elif ((25<n)and(n<=50)):
    print("Intervalo (25,50]")
elif ((50<n)and(n<=75)):
    print("Intervalo (50,75]")
elif ((75<n)and(n<=100)):
    print("Intervalo (75,100]")
elif ((n<0) or (n>100)):
    print("Fora de intervalo")
#analise e impresao dos intervalos
