pares = 0
impares = 0
positivos = 0
negativos = 0
#inicailizacao de 4 variaveis
for x in range(5):
    #enquanto x for menor que 5
    numero = int(input())
    #leiturresto de um numero inteiro
    resto = numero%2
    #resto recebe o resto da divisao do numero por 2
    if resto == 0:
        pares += 1
        #se o resto de um numero inteiro for 0 logo ele e par
        #assim se soma mais 1 na variavel pares
    elif resto != 0:
        impares += 1
        #se o resto de um numero inteiro for diferente de 0 logo ele e impar
        #assim se soma mais 1 na variavel impares
    if numero> 0:
        positivos += 1
        #se o numero for possitivo somase mais 1 na variavel possitivos
    elif numero< 0:
        negativos += 1
        #se o numero for negativo somase mais 1 na variavel negativos
print('{} valor(es) par (es)'.format(pares))
print('{} valor(es) impar (es)'.format(impares))
print('{} valores positivo (s)'.format(positivos))
print('{} valores negativo s)'.format(negativos))
#impressao 