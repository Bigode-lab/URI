#retornar todos os valores que divididos por n 
#dentro do intervalo de 1 a 10000 dem resto 2
numero = int(input())
#leitura de um numero inteiro
indice = 1
#numero que ira variando ate chegar em 10000
while indice < 10000:
    #enquanto indice for menor que 10000
    resto = indice%numero
    #resto vair receber o resto da divisao de indice por numero
    if resto == 2:
        #se o resto for igual a 2
        print(indice)
        #impressao do indice atual
    indice += 1
    #isso e o mesmo que indice = indice + 1
    #indice recebe + 1