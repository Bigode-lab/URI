#apresentar 6 numeros impares a partir de um numeroqualquer
numero = int(input())
#leitura de um numero inteiro
resto =  n%2
#resto recebe o resto da divisao desse numero por 2
if a == 0:
    #se o resto for sero o numero e par
    numero+= 1
    #numero recebe + 1 para que ele se torne impar
    #esse sera o primeiro numero da sequencia
    for x in range(6):
        #enquanto x for menor que 6, fazendo com que o laco rode 6 vezes
        print(numero)
        #impressao do numero
        numero+= 2
        #soma se +2 a numero 
        #assim chegando ao proximo impar
elif a != 0:
    #se o numero for impar
    for x in range(6):
        #enquanto x for menor que 6, fazendo com que o laco rode 6 vezes
        print(numero)
        #impressao do numero
        numero+= 2
        #soma se +2 a numero 
        #assim chegando ao proximo impar