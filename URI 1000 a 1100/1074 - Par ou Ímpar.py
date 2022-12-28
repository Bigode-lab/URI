#dado uma quantidade de casos julgar se cada numero de cada caso
# é impar, par, positivo ou negativo ou zero
casos = int(input())
#leitura de um numero inteiro que sera a quantidade de casos
for x in range(casos):
    #enquando x for menor que casos
    numero = int(input())
    Q#leitura de um numero inteiro
    resto = numero%2
    #resto recebe o resto da divisao do numero por 2
    if resto == 0 and numero <0:
        #se o resto for 0, ou seja, o numero for par
        #e o numero for maior que 0, ou seja, positivo
        print('EVEN NEGATIVE')
        #impressao do resultado
    elif resto == 0 and numero >0:
        #se o resto for 0, ou seja, o numero for par
        #e o numero for menor que 0, ou seja, negativo
        print('EVEN POSITIVE')
        #impressao do resultado
    elif resto != 0 and numero < 0:
        #se o resto for diferente de 0, ou seja, o numero for impar
        #e o numero for menor que 0, ou seja, positivo
        print('ODD NEGATIVE')
        #impressao do resultado
    elif resto != 0 and numero > 0:
        #se o resto for diferente de 0, ou seja, o numero for impar
        #e o numero for maior que 0, ou seja, negativo
        print('ODD POSITIVE')
        #impressao do resultado
    else:
        #se nao entrar em nenhum dos casos aneriores ou seja o numero é zero
        print('NULL')
        #impressao do resultado