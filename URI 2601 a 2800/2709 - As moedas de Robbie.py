#erro de tempo
primo = [2]
cont = 2
#iniciando uma lista que armazenaras os primos encontrados 
def primos(cont, primo, verificador, n):
    #funacao que encontrar os primos ate um numero n e retornara a lista
    while cont <= n:
        for x in primo:
            if cont % x == 0:
                verificador = False
                break
        if  verificador:
            primo.append(cont)
            True
        if n == cont:
            r = verificador
        cont +=1
        verificador = True
    return primo, cont-1, r
while True:
    primo = (primos(cont, primo, True, 10000))            
    try:
        soma = 0
        moedas = []
        quantidade = int(input())
        #leitura da quantidade de moedas
        for x in range(quantidade):
            moeda = int(input())
            moedas.append(moeda)
            #leitura de cada uma das moedas e armzenando as em uma lista
        pulo = int(input())
        for x in range(0,quantidade, pulo):
            soma += moedas[x]    
        if soma in primo:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except EOFError():
        break