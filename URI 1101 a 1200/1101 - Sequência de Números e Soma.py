#ler um conjunto não determinado de pares e mostrar para cada par
#a sequencia do menor ate o maior e a soma dos inteiros
soma = 0
#essa varaivel que vai armazena a soma dos inteiros dentro do intervalo de a e b
j = True
#j sera uma variavel sentinela que e usada como condicional de parada do programa
#declaracao das variaveis
while j:
    #esse while rodara enquando j for verdadeiro
    a, b = (int(x) for x in input().split())
    #leitura de dois  numeros a e b
    menor = min(a, b)
    #menor vai receber o menor numero entre a e b
    maior = max(a, b)
    #maior vai receber o maior numero entre a e b
    if menor > 0 and maior > 0:
        #se menor e maior forem maior do que 0
        while menor <= maior:
            #enquanto menor for menor igual a maior
            print("{}".format(n), end= ' ')
            #imrpressao do numero com no fim tendo uma espaco e nao uma quebra de linha
            soma += n
            #soma recebe +1
            n += 1
            #n recebe +1
        print('Sum={}'.format(soma))
        #impresao da soma ao fim do laco
        soma = 0
        #zeramos a variavel soma 
    else:
        j = False
        #j recebe falso, o que dara fim ao programa