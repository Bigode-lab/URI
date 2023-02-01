#imprimir uma saida apresentada no enunciado#coelho recebe a quantidade de coelhos
i = 1
j = 7
#inicializacao das variaveis
while i <= 9:
    #enquanto i for menor que 9
    for x in range(3):
        #enquando x for menor que 3
        print('I={} J={}'.format(i, j-x))
        #impressao dos respectivos valores de i e j
    i += 2
    j += 2
    #incrementacao de i e j em +2