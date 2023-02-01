#objetivo traduzir a mensagem do corvo
grito = 0
soma  = 0
#inicializacao das variaveis grito e soma
while grito < 3:
    #enquanto grito for menor que 3
    s = input()
    #s recebe uma string
    if s == 'caw caw':
        #se s for caw caw
        grito += 1
        #gruto recebe +1
        print(soma)
        #impressao da soma
        soma = 0
        #soma e zerada
    else:
        for x in range(3):
            #enquanto x for menor que 3
            if s[x] == '*' and x == 0:
                #se s[x] for igual a * e x for igual a 0 
                soma += 4
                #somase mais 4 a soma
            if s [x] == '*' and x == 1:
                #se s[x] for igual a * e x for igual a 1
                soma += 2
               #somase mais 2 a soma 
            if s [x] == '*' and x == 2:
                #se s[x] for igual a * e x for igual a 1
                soma += 1
                #somase mais  a soma