medidas = int(input())
altura = [int(x) for x in input().split()]
if medidas == 1:
    print(0)
elif medidas == 2 and altura[0] == altura[1]:
    print(0)
elif medidas == 2 and altura[0] != altura[1]:
    print(1)    
else:
    s = 1
    cont = 0
    maior = altura[0] > altura[1]



    if maior:
        if medidas%2 == 0:
            for x in range(0,medidas, 2):
                if  (altura[x] <= altura[x+1]):
                    s = 0
                    break

        elif medidas%2 == 1:
            for x in range(0,medidas, 2):
                if x == (medidas-1):
                    break
                elif (altura[x] <= altura[x+1]):
                    s = 0
                    break
                
        print(s)
'''
    else:
        if medidas%2 == 0:
            for x in range(0,medidas, 2):
                if  (altura[x] >= altura[x+1]):
                    s = 0
                    break

        elif medidas%2 == 1:
            for x in range(0,medidas, 2):
                if x == (medidas-1):
                    break
                elif (altura[x] >= altura[x+1]):
                    #print(f'atual = {altura[x]} proximo = {altura[x+1]} cont = {cont}')
                    #print(f'a = {altura[x] <= altura[x+1] and x%2 == 1}')
                    #print(altura[x] >= altura[x+1] and x%2 == 0)
                    s = 0
                    break
                cont+= 1
        print(s)
'''