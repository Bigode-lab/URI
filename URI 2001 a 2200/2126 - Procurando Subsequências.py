caso = 0
#iniciando a vvariavel caso
while True:
    try:
        caso += 1
        #somando mais 1 a casos
        n = input()
        #leitura do primeiro numero
        n1 = input()
        #leitura do segundo numero
        indice = 0
        ocorrencia = 0
        #iniciando variavei indice e occorencia
        #ocorrendia armazenara a quantidade de vezes que n se repete em n1
        for s in n1:
        #percorrendo o segundo n1
            if s == n[0] and ((indice + len(n)) <= len(n1)):
            #se s for igual ao primeiro digito de n1 e a quantidade de numeros apos s for superior ou igual a quantidade de digitos contidos em n
                if n1[indice:(indice + len(n))] == n:
                #veerificamos se o n esta contido em n1
                    pos = indice
                    #pos recebe o indice de ontem comeca n no n1
                    ocorrencia += 1
                    #e somamos 1 a ocorrencia 
            indice += 1
            #somamso mais 1 a indice
        if ocorrencia != 0:
            print(f'Caso #{caso}:\nQtd.Subsequencias: {ocorrencia}\nPos: {pos+1}')
            print('')
            #se tiver alguma ocorrencia imprimos o caso, a quantidade de ocorrencias e aonde se inicia a ultima ocorrencia
        else:
            print(f'Caso #{caso}:')
            print('Nao existe subsequencia')
            print('')
            #se nao umprimimos o caso e que nao a ocorrencia
    except EOFError:
        break
