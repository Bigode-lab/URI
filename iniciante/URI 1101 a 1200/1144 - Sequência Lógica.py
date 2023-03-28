#escreva um codigo que apresente a saida n vezses seguindo a logica do exemplo

#logica da saida
#a saida e uma sequencia de 3 numeros sendo que o primeiro numero varia a cada 2 linhas
#e acaba quando o primeiro numero for igual ao n de entrada
#a primeira linha de saida de cada primeiro numero  da sequencia se da da segunte forma 
    #o primeiro numero e a base
    #o segundo e a base ao quadrado
    #o terceiro a base ao cubo
##a segunda linha de saida de cada primeiro numero  da sequencia se da da segunte forma 
    #o primeiro numero e a base
    #o segundo e a base ao quadrado +1
    #o terceiro a base ao cubo +1
n = int(input())
#leintura de um numero inteiro 
for x in range(n):
    #enquando x for menor que 5
    print('{} {} {}'.format((x+1), ((x+1)**2), ((x+1)**3)))
    #impressao da primeira linha antes da variacao do  numero.
    #a base recebe x+1 pois no laco for o x se inicia em 0 
    print('{} {} {}'.format((x+1), (((x+1)**2)+1), (((x+1)**3)+1)))
    #impressao da primeira linha antes da variacao do  numero.
    #a base recebe x+1 pois no laco for o x se inicia em 0 