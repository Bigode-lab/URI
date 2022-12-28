#indentificar a quantidade de valores pares dentro de 5 numeros
pares = 0
#inicializaçao da variavel
for x in range(5):
    #enquanto x for menor que 5
    numero = float((input()))
    #leitura de um numero de ponto flutuante
    a = numero%2
    #verificando que o numero e par, pois se ele for par ele e divisivel por 2
    if a == 0:
        pares += 1
        #se o numero for divisiel par somase mais 1 em pares
print('{} valores pares'.format(pares))
#impressao da quantidade de numeros pares