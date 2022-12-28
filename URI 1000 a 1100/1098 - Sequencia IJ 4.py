#imprimir uma saida apresentada no enunciado#coelho recebe a quantidade de coelhos
i = 0
j = 1
cont = 5
#inicializacao das variaveis
while i <= 2:
    #enquanto x for menor que 2
    if cont == 5:
        #quando o contador for 5
        for x in range(3):
            #enquanto x for menor que 3
            print('I={:.0f} J={:.0f}'.format(i, j+x))
            #impressao dos respectivos valores de i e j
            cont = 0
            #reiniciando o contador
    else:
        #se nao
        for x in range(3):
            #enquanto x for menor que 3
            print('I={:.1f} J={:.1f}'.format(i, j+x))
            #impressao dos respectivos valores de i e j
    i += 0.2
    j += 0.2
    cont += 1
    #inclementacao das variaveis