#retornar a soma dos umeros impares no intervalo de a e b
casos  = int(input())
#leitra de um numero que e o numerod e casos
for x in range(casos):
    #equanto x for menor que casos
    a , b = (int(x) for x in input().split(' '))
    #leitura de dois numeros
    soma = 0
    #inicializando a variavel soma
    maior  = max(a, b)
    #maior vai receber o maior valor entre a e b
    menor = min(a, b)
    #menor vai receber o menor valor entre a e b
    if maior == menor:
        #se maio r menor forem iguais nao existe intervalo inteiro entre eles
        soma = 0
        #a soma e 0
        print(soma)
        #impressao da soma
    elif maior > menor:
        #se maior for maior que o menor 
        while menor < maior:
            #equanto menor for menor que o maior
            menor += 1
            #menor recebe +1 pois o menor nao esta dentro do intervalo
            resto = menor%2
            #resto recebe o resto da divisao entre menor e 2
            if resto != 0 and maior!=menor:
                #se o resto for diferente de 0 o numero e impar e se maior for diferete de menor
                soma += menor
                #soma e implementada em menor
        print(soma)
        #impressao da soma
