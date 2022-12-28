#ler 100 numeros e retornar o maior valor e sua posicao
for x in range(100):
    #enquanto x for menor que 100
    numero = int(input())
    #leitura de um numero inteiro
    if x == 0:
        #quando x for 0, ou seja, a primeira interaco do loop
        maior = numero
        #maior recebe numero
        posição = x + 1
        #posicao recebe x + 1 pois com x inicia em 0 entao esta sempre uma possicao atras
    if numero > maior:
        #se numero for maior do que o maior numero lido ate o momento
        maior = numero
        #maior recebe numero
        posiçao = x + 1 
        #posicao recebe a posicao do maior numero
print(maior)
#impressao do maior numero
print(posiçao)
#impressao da posicao do maior numero