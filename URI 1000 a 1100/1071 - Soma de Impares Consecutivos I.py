#apressentar a soma de numeros impares entre dois numeros
somresto = 0
#iniciando a variavel soma
n1 = int(input())
#leituro do primeiro numero
n2 = int(input())
#leitura do segundo numero
resto = n2%2
#resto recebe o resto do n2 dividido por 2
if resto == 0 and n1!= n2:
    #se o resto for 0, ou seja, se o numero por par
    #e o n1 diferente do n2, para q eaxista um intervalo de numeros inteiros entre eles
    n2 += 1
    #tornando o n2 um numero impar
    while n2 < n1:
        #enquanto o n2 for menor que n1
        soma += n2
        #soma se o valor de n2 a soma
        n2 += 2
        #isso e o mesmo que n2 = n2 + 2
        #n2 recebe mais dois para que possa se chegar ate o proximo impar
elif resto != 0 and n1!= n2:
    #se o resto for diferente de 0, ou seja, o numero for impar
    #e o n1 diferente do n2, para q eaxista um intervalo de numeros inteiros entre eles
    n2 += 2
    #soma se +2 a n2 para se chegar ao primeiro impar apos ele
    while n2 < n1:
        #enquanto o n2 for menor que n1
        soma += n2
        #soma se o valor de n2 a soma
        n2 += 2
        #isso e o mesmo que n2 = n2 + 2
        #n2 recebe mais dois para que possa se chegar ate o proximo impar
print(soma)
#impressao da soma