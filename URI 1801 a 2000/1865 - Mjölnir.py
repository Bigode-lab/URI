#objetivo: dizer quem consegue e quem nao consegue levantar o mjonir 
casos = int(input())
#leitura de um inteiro que representa a quantidade de casos
for x in range(casos):
    #enquanto x for menor que casos
    nome, forca = (str(x) for x in input().split())
    #leitura do nome dda forca aplicada para levantar o mjonir
    if nome == 'Thor':
        print('Y')
        #se for o thor imprimimos Y pois ele consegue levantar o mjonir
    else:
        print('N')
        #se nao imprimimos N pois ninguem alem do thor consegue
