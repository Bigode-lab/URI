r = 0 
#iniciando a variavel r
a = int(input())
b = int(input())
#leitura de dois valores inteiros a e b
menor = min(a, b)
maior = max(a, b)
#encontrando a maior e o menor numero entre a e b
if maior > menor:
    while menor <= maior: 
        #enquandto menor menor igual a maior
        t = menor%13
        #t recebe o resto da divisao de menor por 13
        if t != 0:
            #se ter for diferente de zero
            r += menor
            #somamos o valor de menor a r, r armazena a soma de numeros que nao sao divisiveis por 13 no interrvalo de a e b 
            menor += 1
            #somamos +1 a menor
        else:
            menor += 1
            #se t for igual a 0, apenas somamos mais um a menor 
print(r)
#imprimimos o valor de r